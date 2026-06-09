const imageInput =
document.getElementById("imageInput");

const preview =
document.getElementById("preview");

imageInput.addEventListener(
    "change",
    function(){

        const file =
        imageInput.files[0];

        if(file){

            preview.src =
            URL.createObjectURL(file);

            preview.style.display =
            "block";
        }
    }
);

async function predictDigit(){

    const file =
    imageInput.files[0];

    if(!file){

        alert(
            "Please upload an image"
        );

        return;
    }

    const formData =
    new FormData();

    formData.append(
        "file",
        file
    );

    try{

        document.getElementById(
            "result"
        ).innerHTML="Loading the results............";
        
        const response =
        await fetch(
            "https://digit-recognition-cnn-arau.onrender.com/predict",
            {
                method:"POST",
                body:formData
            }
        );

        const data =
        await response.json();

        document.getElementById(
            "result"
        ).innerHTML =
        "Predicted Digit : " +
        data.prediction;

    }
    catch(error){

        console.error(error);

        document.getElementById(
            "result"
        ).innerHTML =
        "Error connecting to API";
    }
}