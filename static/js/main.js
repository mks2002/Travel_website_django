let nav = document.querySelector('.navbar');
window.onscroll = function () {
   if (document.documentElement.scrollTop > 50) {
      nav.classList.add("header-scrolled");
   } else {
      nav.classList.remove("header-scrolled");
   }
}

let navbar = document.querySelectorAll(".nav-link");
let navcollapse = document.querySelector(".collapse.navbar-collapse");

navbar.forEach(function (e) {
   e.addEventListener("click", function () {
      navcollapse.classList.remove("show");
   })
});



var swiper = new Swiper(".mySwiper", {
   direction: "vertical",
   loop: true,
   spaceBetween: 30,
   effect: "fade",
   pagination: {
      el: ".swiper-pagination",
      clickable: true,
   },
   autoplay: {
      delay: 3500,
   },
});




document.addEventListener("DOMContentLoaded", () => {

   function counter(id, start, end, duration) {
      let obj = document.getElementById(id),
         current = start,
         range = end - start,
         increment = end > start ? 1 : -1,
         step = Math.abs(Math.floor(duration / range)),
         timer = setInterval(() => {
            current += increment;
            obj.textContent = current;
            if (current == end) {
               clearInterval(timer);
            }
         }, step);
   }
   counter("count1", 0, 1287, 3000);
   counter("count2", 100, 5786, 2500);
   counter("count3", 0, 1440, 3000);
   counter("count4", 0, 7110, 3000);
});






var swiper = new Swiper(".our-partner", {
   slidesPerView: 5,
   spaceBetween: 30,
   loop: true,
   autoplay: {
      delay: 2000,
   },
   breakpoints: {
      '991': {
         slidesPerView: 5,
         spaceBetween: 10,
      },
      '767': {
         slidesPerView: 3,
         spaceBetween: 10,
      },
      '320': {
         slidesPerView: 2,
         spaceBetween: 8,
      },


   },
});


