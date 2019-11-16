async function myFunction(){
    let headingElement = document.querySelector("#photo_wrapper");
    const response2 = await fetch('/api').then(response => response.json());
    //headingElement.textContent = response2;
    document.getElementById("photo1").src = response2[0];
    document.getElementById("photo2").src = response2[1];
    document.getElementById("photo3").src = response2[2];
    document.getElementById("photo4").src = response2[3];
}