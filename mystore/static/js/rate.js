
function addScore(score, $domElement, element) {
    var starWidth = `<style>#${element} .stars-container:after { width: ${score}% ;} </style>`;
    $(`<span class='stars-container'>`)
      .text("★★★★★")
      .append($(starWidth))
      .appendTo($domElement);
}

function rate(rate, element) {  
  addScore(rate * 100 / 5, $(`#${element}`), element)
}