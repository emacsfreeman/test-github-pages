$(document).ready(function(){
  $('.button').click(function() {
    var answer = prompt("What’s your name, sir?");
    console.log(answer);
  });

  $('.button').click(function() {
    console.log("The guests have arrived.");
  });

  $('button').click(function() {
    $.get('http://ask.com', function(data) {
      console.log("Ma’am, your data has arrived:", data);
    });
  });
});
