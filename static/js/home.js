let counter = 0;

const test = $("form section")

function nextButton(){
    $("#next-filter-button").click(function(){
      counter++;
      $("#back-filter-button").prop("disabled", false);
      $("form section").hide();
      $(test[counter]).fadeIn(500);
      if(counter >= test.length -1){
          $("#next-filter-button").prop("disabled", true);
          $("#submit-button").show()
      }
  });
}

function previousButton(){
    $("#back-filter-button").click(function(){
      counter--;
      $("#next-filter-button").prop("disabled", false);
      $("#submit-button").hide()
      $("form section").hide();
      $(test[counter]).fadeIn(500);
      if(counter <= 0){
        $("#back-filter-button").prop("disabled", true);
      }
    });
}

$("#submit-button").click(function(){
  $("#filter-form").hide();
  $("#book-animation-search").show();
  setTimeout(function(){
      $("#filter-form").submit();
  } ,3000)
})




nextButton()
previousButton()
