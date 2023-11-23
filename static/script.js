let btnEle = document.getElementById('redirect')
      let loader = document.querySelector(".progress-bar")
      let hider = document.querySelector(".hide")
      let conEle = document.querySelector(".box")

      btnEle.onclick = function(){
        conEle.style.display = "none";
        loader.style.display = "block";


        setTimeout(function(){
          loader.style.display = "none";
          window.open("{% url 'vulnerability'%}", "_self")
        },15000)
      }