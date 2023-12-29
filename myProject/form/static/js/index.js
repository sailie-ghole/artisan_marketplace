async function validateEmail() {
        const emailInput = document.getElementById('email');
        const validationResult = document.getElementById('validationResult');
        const email = emailInput.value.trim();
        const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
        console.log(email);
        
        const url = 'https://api.zerobounce.net/v2/validate';
        const zeroBounce = new ZeroBounce({ apiKey:
        'ce88d9bcffe146dfacbf216d4a173a37' });
        try {
        const response = await zeroBounce.validateEmail(email);
        console.log(response);
        } catch (error) {
        console.error(error);
        }
 }
    
let generatedOTP = "";

// OTP Generator
function generateOTP(length) {
    const charset = "0123456789";
    let OTP = "";
    for (let i = 0; i < length; i++) {
    const randomIndex = Math.floor(Math.random() * charset.length);
    OTP += charset[randomIndex];
    }
    return OTP;

}

// OTP Checker
function checkOTP(inputOTP) {
    return inputOTP === generatedOTP;
}


const serviceID = "service_mh4zlc4";
const templateID = "template_45wcszs";

// Handle generate button click
document.addEventListener('DOMContentLoaded', function () {
    // Handle generate button click
    document.getElementById("generateButton").addEventListener("click", function () {
        const otpLength = 6;
        generatedOTP = generateOTP(otpLength);
        const params = {
            name: "user",
            email: document.getElementById("email"),
            OTP: generatedOTP,
        };
        console.log("Generated OTP:", generatedOTP);
        emailjs.send(serviceID, templateID, params)
            .then((res) => {
                console.log("OTP SENT");
            })
            .catch((err) => console.log(err));
    });
});

    

// Handle form submission
document.addEventListener('DOMContentLoaded', function () {
    // Handle submitOTP button click
    document.getElementById("submitOTP").addEventListener("click", function () {
        const userInputOTP = document.getElementById("otpEntered").value;
        const isValidOTP = checkOTP(userInputOTP);
        const resultElement = document.getElementById("result");

        if (isValidOTP) {
            resultElement.textContent = "OTP is valid. Click on Next.";
            resultElement.classList.remove("invalid-text"); // Remove red color class
            resultElement.classList.add("valid-text"); // Add green color class
            console.log("valid");
        } else {
            resultElement.textContent = "Invalid OTP. Please try again.";
            resultElement.classList.remove("valid-text"); // Remove green color class
            resultElement.classList.add("invalid-text"); // Add red color class
            console.log("invalid");
        }
    });
});

