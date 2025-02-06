photos = document.getElementsByClassName("takephoto");

for (let i = 0 ; i < photos.length; i++) {
    photos[i].addEventListener("click", () => {
        x = photos[i].parentNode;
        newdiv = document.createElement("img");
        newdiv.src = "http://" + photos[i].value + "/camera/snap";
        x.appendChild(newdiv);
    })
}