//////////////////////////////////
/*Java Scriiop*/

$(function () {
  //execute when the js-menu-icon js clicked

  $(".js-menu-icon").click(function () {
    //$(this) : selft element,namely div . js-menu-icon
    //next() : to div js-menu-icon, namely div menu
    // toggle(): swith show and me hide
    $(this).next().toggle();
  });
});

$(function () {
  //execute when the js-menu-icon js clicked

  $(".btn1").click(function () {
    var btnvar1 = document.getElementById("btnh1");
    let contlike = document.getElementById("cont");

    if (btnvar1.style.color == "red") {
      btnvar1.style.color = "grey";
    } else {
      btnvar1.style.color = "red";
    }

    let cant = parseInt(contlike.textContent);
    let cont = 0;
    if (cant != cont) {
      contlike.textContent = cant -= 1;
    } else {
      contlike.textContent = cant += 1;
      cont = parseInt(contlike.textContent);
    }
  });
});
