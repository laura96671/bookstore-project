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

function submitForm(){
    $("form").validate();
    $("#filter-form").hide();
    $("#next-filter-button").hide();
    $("#back-filter-button").hide();
    $("#submit-button").hide();
    $("#book-animation-search").show();
    setTimeout(function(){
      $("#filter-form").submit();
    } ,3000)
}

function testing(){
    $("#filling-required").show()
}

function viewMore(idx, displayAll){
  const paragId = `#description-text_${idx}`
  const paragIdAll = `#description-all_${idx}`

  let displayVal = "block";
  let displayValAll = "none";

  if(displayAll){
    displayVal = "none";
    displayValAll = "block";
  }

  $(paragId).css("display", displayVal)
  $(paragIdAll).css("display", displayValAll)

}

nextButton()
previousButton()
