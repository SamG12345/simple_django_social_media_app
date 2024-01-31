document.addEventListener("DOMContentLoaded", function (){
    // Like action
    var likeButtons = document.querySelectorAll(".like-button");
    if (likeButtons) {
        likeButtons.forEach(element => {
            element.addEventListener("click", function(e) {
                var lekhId = e.currentTarget.closest('.lekh');
                likeHandler(e, lekhId);
            });
        });
    }

    function likeHandler(e, lekhId) {
        const url = "/like/" + lekhId.dataset.lekhId;
        fetch(url, {
            method: "GET"
        }).then(response => response.json()).then(data => {
            console.log(data.message);
            var likeCountElement = lekhId.querySelector('#no_of_likes');
            var likebuttonelement = lekhId.querySelector('.like-button');
            var value = likeCountElement.innerText;
            var split = value.split(" ");
            
            
            if(data.message == "Liked"){
                split[0] = Number(split[0])+1;
                likeCountElement.innerText = split.join(" ");
                likebuttonelement.innerText = "Unlike";
                
            }
            else if(data.message == "Unliked"){
                split[0] = Number(split[0])-1;
                likeCountElement.innerText = split.join(" ");
                likebuttonelement.innerText = "Like";
            }
        });
    }

    // like icon action
    var fa = document.querySelectorAll(".fa");
    if (fa){
        fa.forEach(element => {
            if (element.id == "like"){
                like_button_initi(element, false);
            }
            else{
                like_button_initi(element, true);
            }
            element.addEventListener("click", (e)=>{
                var lekhId = e.currentTarget.closest('.lekh');
                likeHandler(e, lekhId);
                var c = element.style.color;
                if (c=="crimson"){
                    element.style.color = "#888";
                }
                else{
                    element.style.color="crimson";
                }
            });
        });
        
    }
    // like icon css
    function like_button_initi(x, b){
        if (b){
            x.style.color="crimson";
        }
        else{
            x.style.color = "#888";
        }
    }

    // lekh remove confr
    var l_rm_c = document.querySelectorAll("#l_rm");
    if (l_rm_c){
        l_rm_c.forEach(element => {
            element.addEventListener("click", (e)=>{
                var ol = document.querySelector(".overlay");
                ol.style.display = "block";
                var oll = ol.getElementsByTagName("button");
                oll[0].addEventListener("click", ()=>{
                    ol.style.display = "none";
                });
                oll[1].addEventListener("click", (e)=>{
                    var lekhId = e.currentTarget.closest('.lekh');
                    console.log(lekhId);
                    e.preventDefault();
                    return;
                    l_rm(e, lekhId);
                });
                
            })
        })
    }
    // lekh del
    function l_rm (e, lekhid){
        const url = "/leakh/delete/" + lekhid.dataset.lekhId;
        fetch(url, {
            method: "GET"
        }).then(response => response.json()).then(data => {
            if (data.message == "Deleted"){
                e.srcElement.parentElement.parentElement.parentElement.style.display = "none";
                lekhid.style.display = "none";
                var loc = window.location.href;
                var loc_arr = loc.split("/");
                if(loc_arr.length>3){
                    for (let i=loc_arr.length; i>3; i--){
                        console.log(i);
                        loc_arr.pop(i-1);
                    }
                    window.location.href = loc_arr.join("/");
                }
            }
            else{
                e.style.display = "none";
            }
        })
    }
    // lekh remove confr
    var cl_rm_c = document.querySelectorAll("#cl_rm");
    if (cl_rm_c){
        cl_rm_c.forEach(element => {
            element.addEventListener("click", (e)=>{
                var ol = document.querySelector(".overlay");
                ol.style.display = "block";
                var oll = ol.getElementsByTagName("button");
                oll[0].addEventListener("click", ()=>{
                    ol.style.display = "none";
                });
                oll[1].addEventListener("click", (e)=>{
                    var i = element.parentElement.parentElement;
                    l_rm(e, i);
                });
                
            })
        })
    }
    var pp = document.querySelector(".profile-img-container");
    if(pp){
        console.log("ok", pp);
        var ppp = document.querySelector("#pp");
        console.log(ppp);
        ppp_ch = ppp.children[0].children;
        ppp_ch[0].addEventListener("click", ()=>{
            console.log("new = ", ppp_ch[2].children[0].children[1]);
            ppp_ch[2].children[0].children[1].click();
        })
        ppp_ch[1].addEventListener("click", ()=> {
            ppv(pp);
        })
        console.log("ok = ", ppp_ch[2].children[0].children[1]);
        ppp_ch[2].children[0].children[1].addEventListener("change", (e) => {
            console.log("ok = ", ppp_ch[2].children[0].children[0]);
            var f = new FormData(ppp_ch[2].children[0]);
            console.log(ppp_ch[2].children[0]);
            pp_chng(f);

        })
        console.log(ppp_ch);
    }

    function ppv(pp){
        var a = pp.children[1].children[0].src;
        window.location.href = a;
    }
    function pp_chng(f){
        fetch("profile_image_upload", {
            method: "POST",
            body: f
        }).then(response => response.json()).then(data => {
            if (data.message == "uploaded"){
                window.location.href=window.location.href;
            }
            else{
                console.log("eror");
            }
        })
    }
    var comp = document.querySelectorAll("#comp");
    if (comp){
        comp.forEach(element => {
            element.addEventListener("click", (e)=>{
        
                console.log(e.target.parentElement.parentElement.id);
                var id = e.target.parentElement.parentElement.id;
                var url = "/comp/"+id;
                fetch(url, {
                    method: "GET",
                }).then(response => response.json()).then(data => {
                    if (data.message == "compaining"){
                        e.target.innerText = "Uncompane";
                    }
                    else{
                        e.target.innerText = "Compane";
                    }
                    console.log(data);
                })
            })
        })
    }
    function inc(){
        var loc = window.location.href;
        var loc_arr = loc.split("/");
        if(loc_arr.length>3){
            for (let i=loc_arr.length; i>3; i--){
                loc_arr.pop(i-1);
            }
            return loc_arr.join("/");
        }
        return loc;
    }
    var l_shr = document.querySelectorAll("#l_shr");
    if(l_shr){
        l_shr.forEach(element => {
            element.addEventListener("click", () => {
                console.log("ok");
                navigator.clipboard.writeText(window.location.href);
            })
        })
    }
    
})

