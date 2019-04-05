function addColors() {
    var colors = new Array('#96B096', '#F2DDC0', '#F2D8AD', '#e4bae3', '#f2e1b9', '#efdfa2', '#AAA17D', '#CED9C2', '#E7C8A4'); 

    var div = document.getElementsByTagName("span");

    for (var i=0; i<div.length; i++) {
        div[i].style.backgroundColor=colors[Math.round(Math.random()*(colors.length-1))];
    }
    document.getElementById("navbar").style.backgroundColor="beige";
}
