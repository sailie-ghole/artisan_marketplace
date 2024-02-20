from django.shortcuts import render, redirect
# from form.models import Student
from form.models import Location
from form.models import Artwork
from form.models import Payment
from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from django.views.decorators.csrf import csrf_exempt
import json
import folium
import geocoder
from .models import Search
from .forms import SearchForm
# import razorpay


def home(request):
    return render(request,"form/index.html")

def formInput(request):
    return render(request,"form/formInput.html")

# def addData(request):
#     if request.method == 'POST':
#         reg_id = request.POST['reg_id']
#         fname = request.POST['fname']
#         lname = request.POST['lname']
#         gender = request.POST['gender']
#         cgpa = request.POST['cgpa']
#         branch = request.POST['branch']
#         email = request.POST['email']
#         phone = request.POST['phone']
#         image = request.FILES['image']
#         bio = request.POST['bio']
        
#         student = Student.objects.create(
#             reg_id = reg_id,
#             fname = fname,
#             lname = lname,
#             gender = gender,
#             cgpa = cgpa,
#             branch = branch,
#             email = email,
#             phone = phone,
#             image = image,
#             bio = bio
#         )
#         student.save()

#         return redirect(formInput)
    



def addData(request):
    if request.method == 'POST':
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        gender = request.POST['gender']
        phone = request.POST['phone']
        url = request.POST['url']
        medium = request.POST['medium']
        title = request.POST['title']
        bio = request.POST['bio']
        price = request.POST['price']
        image = request.FILES['image']
        location = request.POST['location']
        
        artwork = Artwork.objects.create(
            email = email,
            fname = fname,
            lname = lname,
            gender = gender,
            phone = phone,
            url = url,
            medium = medium,
            title = title,
            bio = bio,
            price = price,
            image = image,
            location = location,
        )
        artwork.save()

        return redirect(formInput)    
    
def showData(request):
    all_artworks = Artwork.objects.all()
    context = {'all_artworks':all_artworks}
    return render(request,'form/showData.html',context)    
    

def displayData(request):
    all_artworks = Artwork.objects.all()
    context = {'all_artworks':all_artworks}
    return render(request,'form/displayData.html',context)

def displayDatat(request):
    all_artworks = Artwork.objects.all()
    context = {'all_artworks':all_artworks}
    return render(request,'form/displayDatat.html',context)

def pdf(request):
    return render(request,"form/pdf_template.html")

def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None

#Opens up page as PDF
class ViewPDF(View):
	def get(self, request, name, *args, **kwargs):
            artwork_invoice = Artwork.objects.get(fname = name)
            print("Image URL:", artwork_invoice.image.url)
            
            data = {}
            data["email"] = artwork_invoice.email
            data["fname"] = artwork_invoice.fname
            data["lname"] = artwork_invoice.lname
            data["gender"] = artwork_invoice.gender
            data["phone"] = artwork_invoice.phone
            data["title"] = artwork_invoice.title
            data["medium"] = artwork_invoice.medium
            data["bio"] = artwork_invoice.bio
            data["price"] = artwork_invoice.price
            data["image"] = artwork_invoice.image.url
            
            pdf = render_to_pdf('form/pdf_template.html', data)
            return HttpResponse(pdf, content_type='application/pdf')


# #Automaticly downloads to PDF file
class DownloadPDF(View):
	def get(self, request, name, *args, **kwargs):
		
            artwork_invoice = Artwork.objects.get(fname = name)
                
            data = {}
            data["email"] = artwork_invoice.email
            data["fname"] = artwork_invoice.fname
            data["lname"] = artwork_invoice.lname
            data["gender"] = artwork_invoice.gender
            data["phone"] = artwork_invoice.phone
            data["title"] = artwork_invoice.title
            data["medium"] = artwork_invoice.medium
            data["bio"] = artwork_invoice.bio
            data["price"] = artwork_invoice.price
            data["image"] = artwork_invoice.image.url
                     
            pdf = render_to_pdf('app/pdf_template.html', data)

            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
      

def students(request):
     return render(request, 'form/base_officer.html')

def map_location(request):
    #  we are going to serialize this to a json
     addresses = list(Search.objects.values('lat', 'lng')[:100])
     context={'addresses': addresses}
     return render(request, 'form/map_location.html', context)



# def map(request):
#     if request.method == 'POST':
#         form = SearchForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(map)
#     else:
#         form = SearchForm()
#     address = Search.objects.all().last()
#     location = geocoder.osm(address)
#     lat = location.lat
#     lng = location.lng
#     country = location.country
#     if lat == None or lng == None:
#         address.delete()
#         return HttpResponse('You address input is invalid. Refresh to add correct address.')

#     # Create Map Object
#     m = folium.Map(location=[19, -12], zoom_start=2)
#     folium.Marker([lat, lng], tooltip = 'Click for more',
#                   popup=country).add_to(m)
#     # Get HTML Representation of Map Object
#     m = m._repr_html_()
#     context = {
#         'm': m,
#         'form': form,
#     }
#     return render(request,'form/map.html', context)



def map(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data['address']
            location = geocoder.osm(address)
            lat = location.lat
            lng = location.lng

            if lat is not None and lng is not None:
                # Save the form data along with latitude and longitude
                search = form.save(commit=False)
                search.lat = lat
                search.lng = lng
                search.save()
                return redirect('map')
            else:
                return HttpResponse('Invalid address. Refresh to add a correct address.')

    else:
        form = SearchForm()

    address = Search.objects.last()

    # Create Map Object
    m = folium.Map(location=[19, -12], zoom_start=2)
    if address:
        folium.Marker([address.lat, address.lng], tooltip='Click for more', popup=address.address).add_to(m)
    # Get HTML Representation of Map Object
    m = m._repr_html_()
    context = {
        'm': m,
        'form': form,
    }
    return render(request, 'form/map.html', context)


# # def fees(request):
# #     if request.method == 'POST':
# #         amount = 100
# #         order_currency = 'INR'
# #         client = razorpay.Client(
# #             auth=("rzp_test_dDOoLTdfM5ydGA", "KxHWykinif2m1f1VzoDPaKPb"))
# #         payment = client.order.create({'amount':amount, 'currency':'INR', 'payment_capture': '1'})
# #         # client.order.create(data=DATA)
# #     return render(request,'form/fees.html')

# # @csrf_exempt------------------------------------------
# # def success(request):
# #     return render(request,'form/payment_success.html')

def fees(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        amount = int(request.POST.get('amount'))*100
        email= request.POST.get('email')
        fname= request.POST('fname')
        title= request.POST('title')
        client = razorpay.Client(
            auth=("rzp_test_dDOoLTdfM5ydGA", "KxHWykinif2m1f1VzoDPaKPb"))
        payment = client.order.create({'amount':amount, 'currency':'INR', 'payment_capture': '1'})
        # client.order.create(data=DATA)

        info = Payment(
             name=name, 
             email=email, 
             amount=amount, 
             fname=fname,
             title=title,
            #  order_id = payment[id']
             )
        info.save()

        return render(request,'form/fees.html' ,{'payment':payment})
    return render(request,'form/fees.html')

@csrf_exempt
def success(request):
    return render(request,'form/payment_success.html')


def studentsView(request):
    oil_no = Artwork.objects.filter(medium='Oil').count()
    oil_no = int(oil_no)
    print('Number of Oil Painting Artworks Are',oil_no)

    water_no = Artwork.objects.filter(medium='Watercolor').count()
    water_no = int(water_no)
    print('Number of Watercolor Artworks Are',water_no)

    scu_no = Artwork.objects.filter(medium='Sculpture').count()
    scu_no = int(scu_no)
    print('Number of Sculpture Artworks Are',scu_no)

    digi_no = Artwork.objects.filter(medium='Digital').count()
    digi_no = int(digi_no)
    print('Number of Digital Art Artworks Are',digi_no)

    acry_no = Artwork.objects.filter(medium='Acrylic').count()
    acry_no = int(acry_no)
    print('Number of Acrylic Artworks Are',acry_no)

    male_no = Artwork.objects.filter(gender='Male').count()
    male_no = int(male_no)
    print('Number of Male Are',male_no)

    female_no = Artwork.objects.filter(gender='Female').count()
    female_no = int(female_no)
    print('Number of Female Are',female_no)

    total_artworks= oil_no + water_no + scu_no + digi_no + acry_no

    gender_list = ['Male', 'Female']
    gender_number = [male_no, female_no]


    artwork_list = ['Oil','Watercolor', 'Sculpture', 'Digital', 'Acrylic']
    number_list = [oil_no, water_no, scu_no, digi_no, acry_no]
    context = {'artwork_list':artwork_list, 'number_list':number_list, 'gender_list':gender_list, 'gender_number':gender_number, 'total_artworks':total_artworks}
    return render(request, 'form/officer_home.html', context)





# def studentsView(request):
#     it_no = Student.objects.filter(branch='Information Technology').count()
#     it_no = int(it_no)
#     print('Number of CInformation Technology Students Are',it_no)

#     cs_no = Student.objects.filter(branch='Computer Science').count()
#     cs_no = int(cs_no)
#     print('Number of Computer Science Students Are',cs_no)

#     ce_no = Student.objects.filter(branch='Computer Engineering').count()
#     ce_no = int(ce_no)
#     print('Number of Computer Engineering Students Are',ce_no)

#     se_no = Student.objects.filter(branch='Software Engineering').count()
#     se_no = int(se_no)
#     print('Number of Software Engineering Students Are',se_no)

#     sec_no = Student.objects.filter(branch='Computer Security').count()
#     sec_no = int(sec_no)
#     print('Number of Computer Security Students Are',sec_no)

#     male_no = Student.objects.filter(gender='Male').count()
#     male_no = int(male_no)
#     print('Number of Male Are',male_no)

#     female_no = Student.objects.filter(gender='Female').count()
#     female_no = int(female_no)
#     print('Number of Female Are',female_no)

#     total_student = it_no + cs_no + ce_no + se_no + sec_no

#     gender_list = ['Male', 'Female']
#     gender_number = [male_no, female_no]

#     cgpa_list = Student.objects.values('fname', 'cgpa')
#     branch_list = ['Information Technology','Computer Science', 'Computer Engineering', 'Software Engineering', 'Computer Security']
#     number_list = [it_no, cs_no, ce_no, se_no, sec_no]
#     context = {'branch_list':branch_list, 'number_list':number_list, 'gender_list':gender_list, 'gender_number':gender_number, 'total_student':total_student, 'cgpa_list':cgpa_list }
#     return render(request, 'form/officer_home.html', context)


def addmapData(request):
    if request.method == 'POST':
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']
        markerTitle = request.POST['markerTitle']
        
        location = Location.objects.create(
            latitude = latitude,
            longitude = longitude,
            markerTitle = markerTitle,
            
        )
        location.save()
        return redirect(map_location)


def mapData(request):
    all_locations = Location.objects.all()
    context = {'all_students':all_locations}
    return render(request,'form/mapShowData.html',context)


