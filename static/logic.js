
//var response2;

async function myFunction() {
    let headingElement = document.querySelector("#photo_wrapper");
    response2 = await fetch('/api').then(response => response.json());
    window.info = response2;
    console.log(response2);
    for (i = 0; i < 4; i++) {
        document.getElementById("title"+String(i+1)).textContent = response2[i][3];
        document.getElementById("link"+String(i+1)).href = response2[i][4];
        document.getElementById("photo"+String(i+1)).src = response2[i][1];
        document.getElementById("phototext"+String(i+1)).textContent = response2[i][2];
    }
}

async function vote_photo(number) {
    //console.log(window.info[number - 1][0]);
    console.log(window.info);
    const idstr = window.info[number - 1][0];
    let rawResponse = await fetch('/api/vote', {
        method: "POST",
        body: "id="+String(idstr),
        headers:
        {
            "Content-Type": "application/x-www-form-urlencoded"
        }
    });

    window.info[number-1][2] = window.info[number-1][2]+1;

    //body: JSON.stringify({ id: idstr }), // data can be `string` or {object}!
    document.getElementById("phototext"+String(number)).textContent = window.info[number-1][2];
    const content = await rawResponse.json();
    //alert(content.message);

}