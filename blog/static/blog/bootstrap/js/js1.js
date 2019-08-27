
var myimg = document.getElementById('mypics');

imgarray = ['static/blog/imgs/sport.jpg', 'static/blog/imgs/education.jpg', 'static/blog/imgs/entertainment.jpg',
          'static/blog/imgs/lifestyle-font.jpg','static/blog/imgs/fash_world.jpg', 'static/blog/imgs/tech.jpg'];

imgindex = 0;

function changeImg(){
  myimg.setAttribute("src", imgarray[imgindex]);
  imgindex++;
  if(imgindex >= imgarray.length){
    imgindex = 0;
  }
}

setInterval(changeImg, 7000)
