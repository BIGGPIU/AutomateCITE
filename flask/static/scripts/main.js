photos = document.getElementsByClassName("takephoto");
console.log(photos)

for (let i = 0 ; i < photos.length; i++) {
    console.log(photos[i])
    photos[i].addEventListener("click", () => {
        console.log(photos[i])
        x = photos[i].parentNode;
        newdiv = document.createElement("img");
        newdiv.src = "http://" + photos[i].value + ":8000/camera/snap";
        x.appendChild(newdiv);
        photos[i].style = "display:none"; // no more pictures for you
    })
}

