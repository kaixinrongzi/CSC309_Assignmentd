/*
 * controller.js
 *
 * Write all your code here.
 */

var globalErr = [false, false, false, false, false]
var setUsername = false;
var setPwd1 = false;
var setPwd2 = false;
var setPhone = false;
var setEmail = false;
var items = []
var sub_total = 0
var tax = 0
var grand_total = 0
var num_para = 1
var handle_scroll = true


//async function fetch_para(){
//    var response = await fetch("http://localhost:8000/text/data?paragraph=" + num_para, {method: 'GET'})
//    var all_data = await response.json()
//    var data = all_data.data
//    data.forEach((value, index)=>{
//        var number = index + 1
//        var para_id = '#paragraph_' + number
////        console.log(number)
//
////        var new_div = document.createElement('div')
////        new_div.setAttribute('id', 'paragraph_' + number)
//
//        var p = document.createElement('p')
//        p.innerHTML = value.content
//        var b = document.createElement('b')
//        b.innerHTML = ' (Paragraph: ' + number + ')'
//        var likes = document.createElement('button')
//        $(likes).attr({'class': ' btn like'})
//        $(likes).html('Likes: '+value.likes)
//
//        p.appendChild(b)
//        $(para_id).append(p)
//        $(para_id).append(likes)
//
//        num_para += 1
//     })
//
//     if (!all_data.next){
//        handle_scroll = false
//     }
//
////     scroll_to_end_handler()
//
//}

//fetch("http://localhost:8000/text/data?paragraph=" + num_para, {method: 'GET'})
//    .then(response => response.json())
//    .then(data => {
//        data.data.forEach((value, index)=>{
//           var number = index + 1
//           console.log(number)
//
//           var new_div = document.createElement('div')
//           new_div.setAttribute('id', 'paragraph_' + number)
//
//           var p = document.createElement('p')
//           p.innerHTML = value.content
//           var b = document.createElement('b')
//           b.innerHTML = ' (Paragraph: ' + number + ')'
//           var likes = document.createElement('button')
//           $(likes).attr({'class': ' btn like'})
//           $(likes).html('Likes: '+value.likes)
//
//           p.appendChild(b)
//           new_div.appendChild(p)
//           new_div.appendChild(likes)
//
//           $('#data').append(new_div)
//
//           num_para += 1
//        })
//
//        if (!data.next){
//            handle_scroll = false
//        }
//
//    });


//function myStopFunction() {
//  setTimeout(()=>alert("lalala"), 3000);
//}
//
//myStopFunction()

function fun1() {$(document).on("update", "#add_update_item tr", function(){
        $('#subtotal').html(subtotal)
        $('#tax').html(tax)
        $('#grand_total').html(grand_total)
    })
    };


function fun2() {$(document).on("click", ".btn.increase", function(e){

        var row = e.target.closest('tr')
        // 1. update the items
        var name = row.id.replace('_', /\s+/g)
        var n = items.length
        var target_item = null
        for(var i=0; i<n; i++){
            if (items[i].name === name){
                target_item = items[i]
                target_item.quantity++
                target_item.total = target_item.price * target_item.quantity
                break
            }
        }
        row.querySelector('.display_quantity').innerHTML = target_item.quantity
        row.querySelector('.display_total').innerHTML = '$'+target_item.total.toFixed(2)

        sub_total += target_item.price
        tax = sub_total * 0.13
        grand_total = 1.13 * sub_total
        $('#subtotal').html(sub_total.toFixed(2))
        $('#taxes').html(tax.toFixed(2))
        $('#grand_total').html(grand_total.toFixed(2))
    })};


function fun3() { $(document).on("click", ".btn.decrease", function(e){

        var row = e.target.closest('tr')
        // 1. update the items
        var name = row.id.replace('_', /\s+/g)
        var n = items.length
        var target_item = null
        for(var i=0; i<n; i++){
            if (items[i].name === name){
                target_item = items[i]
                if (target_item.quantity === 0){
                    return
                }
                target_item.quantity--
                target_item.total = target_item.price * target_item.quantity
                break
            }
        }
        row.querySelector('.display_quantity').innerHTML = target_item.quantity
        row.querySelector('.display_total').innerHTML = '$'+target_item.total.toFixed(2)

        sub_total -= target_item.price
        tax = sub_total * 0.13
        grand_total = 1.13 * sub_total
        $('#subtotal').html(sub_total.toFixed(2))
        $('#taxes').html(tax.toFixed(2))
        $('#grand_total').html(grand_total.toFixed(2))

    })};


function fun4(){$(document).on("click", ".btn.delete", function(e){

        var row = e.target.closest('tr')
        // 1. update the items
        var name = row.id.replace('_', /\s+/g)
        var n = items.length
        var target_item = null
        var target_index = 0
        var orig_qty = 0
        for(var i=0; i<n; i++){
            if (items[i].name === name){
                target_item = items[i]
                target_index = i
                orig_qty = target_item.quantity
                break
            }
        }
    //    row.querySelector('.display_quantity').innerHTML = 0
    //    row.querySelector('.display_total').innerHTML = '$0.00'

        sub_total -= orig_qty * target_item.price
        tax = sub_total * 0.13
        grand_total = 1.13 * sub_total
        $('#subtotal').html(sub_total.toFixed(2))
        $('#taxes').html(tax.toFixed(2))
        $('#grand_total').html(grand_total.toFixed(2))

        items.splice(target_index, 1)
        row.remove()

    })
    };


function fun5(){$(document).on('click', '.btn.like', function(e){
        const target_div_id = e.target.closest('div').id
        console.log("div id:", target_div_id)
        const target_para_id = parseInt(target_div_id.slice(target_div_id.indexOf('_')+1, ))
        console.log("para id:", target_para_id)

        fetch("/text/like",
        {method: 'POST',
         body: JSON.stringify({paragraph: target_para_id})
        })
        .then(response => response.json())
        .then(data => {
            var likes = data.data.likes
            e.target.innerHTML = "Likes: " + likes
         })
    })
    };


function fun6() {$( "#username" ).change(function(e){
        setUsername = true;
        var username = e.target.value;
        console.log(username);

        var error = false;
        if (username.length < 6){
            error = true
        }
        else{
            for (let char of username){
    //            console.log(char)
                let charCode = char.charCodeAt(0);
                if (!(charCode > 47 && charCode < 58) && !(charCode > 96 && charCode < 123) && !(charCode > 64 && charCode < 91) && !(charCode == 95)
                ) {
                   error = true
                }
            }
        }

        if(error){
            $("#username_notification").html('Username is invalid');
            $(e.target).css("background-color", "red");
            globalErr[0] = true;
        }else{
            $("#username_notification").html('');
            $(e.target).css("background-color", "lightcyan");
            globalErr[0] = false;
        }

        console.log(error)
    })
    };


function fun7() { $( "#password1" ).change(function(e){
        setPwd1 = true;
        var password = e.target.value;
        console.log(password);

        var error = false;
        if (password.length < 8){
            error = true
        }
        else{
            var smallLetter = 0;
            var capital = 0;
            var num_digit = 0;
            var num_sign = 0;
            for (let char of password){
    //            console.log(char)
                let charCode = char.charCodeAt(0);
                if (charCode > 47 && charCode < 58) {   //0-9
                   num_digit += 1;
                }
                else if (charCode > 64 && charCode < 91) {   //0-9
                   capital += 1;
                }
                else if (charCode > 96 && charCode < 123) {   //0-9
                   smallLetter += 1;
                }
                else if (charCode > 64 && charCode < 91) {   //0-9
                   capital += 1;
                }
                else if (char == '!' || char == '@' || char == '#' || char == '$' || char == '%' || char == '^' || char == '&' || char =='*' ){
                    num_sign += 1;
                }
                else{
                }
            }

            if (smallLetter < 1 || capital < 1 || num_digit < 1 || num_sign < 1){
                error = true;
            }

        }

        if(error){
            $("#password1_notification").html('Password is invalid');
            $(e.target).css("background-color", "red");
            globalErr[1] = true;
        }else{
            $("#password1_notification").html('');
            $(e.target).css("background-color", "lightcyan");
            globalErr[1] = false;
        }

        console.log(error)

    })
    };


function fun8(){ $('#password2').change(function(e){
        setPwd2 = true;
        var password2 = e.target.value;
        var password1 = $('#password1').val();
        if (password1 !== password2){
            $("#password2_notification").html("Passwords don't match")
            $(e.target).css("background-color", "red");
            globalErr[2] = true;
        }else{
            $("#password2_notification").html('');
            $(e.target).css("background-color", "lightcyan");
            globalErr[2] = false;
        }
    })
    };


function fun9(){ $('#email').change(function(e){
        setEmail = true;
        var email = e.target.value;
        var regex = /^(([^<>()[\]\\.,;:\s@]+(\.[^<>()[\]\\.,;:\s@]+)*)|.(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
        if(regex.test(email)){ //valid email
            $("#email_notification").html('')
            $(e.target).css("background-color", "lightcyan");
            globalErr[3] = false;
        }else{                 //invalid email
            $("#email_notification").html('Email is invalid')
            $(e.target).css("background-color", "red");
            globalErr[3] = true;
        }
    })
    };


    function fun10() {$('#phone').change(function(e){
        setPhone = true;
        var phone = e.target.value;
        var pattern = new RegExp("^\\d{3}-\\d{3}-\\d{4}$");
        if (pattern.test(phone)) {
            $('#phone_notification').html("");
            $(e.target).css("background-color", "lightcyan");
            globalErr[4] = false;
        } else {
            $('#phone_notification').html("Phone is invalid");
            $(e.target).css("background-color", "red");
            globalErr[4] = true;
        }
    })
    };


 function fun11(){$('#register').click(function(e){
        if (globalErr.indexOf(true) !== -1) {
            $('#notification').html('At least one field is invalid. Please correct it before proceeding')
        }
        if (!setUsername){
           $('#username').css("background-color", "red");
           $("#username_notification").html('Username is invalid');
           $('#notification').html('At least one field is invalid. Please correct it before proceeding')
        }
        if(!setPwd1){
           $('#password1').css("background-color", "red");
           $("#password1_notification").html('Password is invalid');
           $('#notification').html('At least one field is invalid. Please correct it before proceeding')
        }
        if(!setPwd2){
           $('#password2').css("background-color", "red");
           $("#password2_notification").html("Passwords don't match");
           $('#notification').html('At least one field is invalid. Please correct it before proceeding')
        }
        if (!setEmail){
           $('#email').css("background-color", "red");
           $("#email_notification").html("Email is invalid");
           $('#notification').html('At least one field is invalid. Please correct it before proceeding')
        }
        if (!setPhone){
           $('#phone').css("background-color", "red");
           $("#phone_notification").html("Phone is invalid");
           $('#notification').html('At least one field is invalid. Please correct it before proceeding')
        }
        if (setUsername && setPwd1 && setPwd2 && setEmail && setPhone && globalErr.indexOf(true) === -1){
            $('#notification').html('');

            // send to the backend server
//            $.post("register",
//              JSON.stringify({
//                username: $('#username').val(),
//                password1: $('#password1').val(),
//                password2: $('#password2').val(),
//                email: $('#email').val(),
//                phone: $('#phone').val(),
//              }),
//              function(data, status){
//
//              })
//              .fail(function(xhr, status, error) {
//                if (status === 'Conflict'){
//                    $('#username_notification').html('Username has already been taken')
//                }else if (status === 'BAD'){
//                    $('#notification').html('Unknown error occurred')
//                }else{
//
//                }
//              })
//              .done(function() {
//                $('#notification').html('User added')
//              })

              $.ajax({
                   type: "POST",
                   url: "register",
                   data: JSON.stringify({
                            username: $('#username').val(),
                            password1: $('#password1').val(),
                            password2: $('#password2').val(),
                            email: $('#email').val(),
                            phone: $('#phone').val(),
                          }),
                   success: function(result){
                        $('#notification').html('User added')
                   },
                   error: function(request,status,errorThrown) {

                        if (status === 'Conflict'){
                            $('#username_notification').html('Username has already been taken')
                        }else if (status === 'BAD'){
                            $('#notification').html('Unknown error occurred')
                        }else{

                        }
                   }
               }).catch(e=>{

                if (e.status === 409){
                    $('#username_notification').html('Username has already been taken')
                }else if (e.status === 400){
                    $('#notification').html('Unknown error occurred')
                }
               });

        }
    })
    };


function fun12(){$('#add_update_item').click(function(e){
        var name = $('#name').val()
        var price = parseFloat($('#price').val())
        var quantity = $('#quantity').val()
        var total = price * quantity
        var subtotal = parseFloat($('#subtotal').html())

        // check if the input is valid?
        if (name === '' || isNaN(price) || isNaN(quantity)){
            $('#item_notification').html("Name, price, or quantity is invalid")
            return
        }else if(!(/^\d+$/.test(quantity))){
            if(/^\d+\.0+$/.test(quantity)){
                $('#item_notification').html("")
                quantity = parseInt(quantity)
            }else{
                $('#item_notification').html("Name, price, or quantity is invalid")
                return
            }
        }else if(price <= 0){
            $('#item_notification').html("Name, price, or quantity is invalid")
            return
        }else{
             $('#item_notification').html("")
             quantity = parseInt(quantity)
        }

        // check if the name exists in the table already
        var update = false
        var old_item_total = 0
        var n = items.length
        var total_change = parseFloat(price) * parseInt(quantity)
        for (var i = 0; i < n; i++){
            var item = items[i]
            if (item.name === name){
                update = true
                total_change = -parseFloat(item.price) * parseInt(item.quantity) + parseFloat(price) * parseInt(quantity)
                console.log(total_change)
                item.price = parseFloat(price)
                item.quantity = parseInt(quantity)
                item.total = parseFloat(total)
                break
            }
        }

        if(update){
            console.log("update")
            var update_row = $('#cart-items').find('#'+name.replace(/\s+/g, '_'))
            console.log(update_row)
            update_row.find('.display_price').html('$'+price)
            update_row.find('.display_quantity').html(quantity)
            update_row.find('.display_total').html('$'+total)


        }else{
            console.log("not update")
            var new_row = $('<tr><td class="display_name"></td><td class="display_price"></td><td class="display_quantity"></td><td class="display_total"></td>'+
            '<td><button class="btn decrease"> - </button></td><td> <button class="btn increase"> + </button> </td><td> <button class="btn delete"> delete </button> </td></tr>')
            new_row.attr({'id': name.replace(/\s+/g, '_')})
            $('#cart-items tbody').append(new_row);

            var new_item = new Item(name, parseFloat(price), parseInt(quantity), parseFloat(total))
            items.push(new_item)

            $(new_row).find('.display_name').html(name)
            $(new_row).find('.display_price').html('$'+price.toFixed(2))
            $(new_row).find('.display_quantity').html(quantity)
            $(new_row).find('.display_total').html('$'+total.toFixed(2))

        }

        sub_total += total_change
        tax += 0.13 * total_change
        grand_total += total_change * 1.13
        $('#subtotal').html(sub_total.toFixed(2))
        $('#taxes').html(tax.toFixed(2))
        $('#grand_total').html(grand_total.toFixed(2))

    })
    };


function fun13(){ window.addEventListener('scroll', function(){
    if (!handle_scroll){
            return
        }
        // Get the current scroll position and viewport height
        const scrollTop = document.documentElement.scrollTop;
        const windowHeight = window.innerHeight;

        //console.log("scrollTop: ", scrollTop, "windowHeight: ", windowHeight)

        // Get the full document height
        const fullHeight = document.documentElement.scrollHeight;

        // Check if the user has scrolled to the bottom of the page
        if (scrollTop + windowHeight >= fullHeight) {
            // Send a request to your server to fetch more data
            fetch("/text/data?paragraph=" + num_para,
                 {method: 'GET'})
                 .then(response => response.json())
                 .then(data => {

                    if (!data.next){
                        var end_b = document.createElement('b')
                        $(end_b).html('You have reached the end')
                        $('#data').after($(end_b))
                        handle_scroll = false
                    }

                    data.data.forEach((value, index)=>{

                        var new_div = document.createElement('div')
                        new_div.setAttribute('id', 'paragraph_' + value.paragraph)
                        var p = document.createElement('p')
                        p.innerHTML = value.content
                        var b = document.createElement('b')
                        b.innerHTML = ' (Paragraph: ' + value.paragraph + ')'
                        var likes = document.createElement('button')
                        $(likes).attr({'class': ' btn like'})
                        $(likes).html('Likes: '+value.likes)

                        p.appendChild(b)
                        new_div.appendChild(p)
                        new_div.appendChild(likes)

                        $('#data').append(new_div)

                        num_para += 1

                    })

                 })
                 .catch(error => console.error(error))
          }
    })
    }


//var scroll_to_end_handler=()=>{
//    if (!handle_scroll){
//         return
//    }
//
//    window.addEventListener('scroll', () => {
//        if (!handle_scroll){
//            return
//        }
//        // Get the current scroll position and viewport height
//        const scrollTop = document.documentElement.scrollTop;
//        const windowHeight = window.innerHeight;
//
//        //console.log("scrollTop: ", scrollTop, "windowHeight: ", windowHeight)
//
//        // Get the full document height
//        const fullHeight = document.documentElement.scrollHeight;
//
//        // Check if the user has scrolled to the bottom of the page
//        if (scrollTop + windowHeight >= fullHeight) {
//            // Send a request to your server to fetch more data
//            fetch("http://localhost:8000/text/data?paragraph=" + num_para,
//                 {method: 'GET'})
//                 .then(response => response.json())
//                 .then(data => {
//
//                    if (!data.next){
//                        var end_b = document.createElement('b')
//                        $(end_b).html('You have reached the end')
//                        $('#data').after($(end_b))
//                        handle_scroll = false
//                    }
//
//                    data.data.forEach((value, index)=>{
//
//                        var new_div = document.createElement('div')
//                        new_div.setAttribute('id', 'paragraph_' + value.paragraph)
//                        var p = document.createElement('p')
//                        p.innerHTML = value.content
//                        var b = document.createElement('b')
//                        b.innerHTML = ' (Paragraph: ' + value.paragraph + ')'
//                        var likes = document.createElement('button')
//                        $(likes).attr({'class': ' btn like'})
//                        $(likes).html('Likes: '+value.likes)
//
//                        p.appendChild(b)
//                        new_div.appendChild(p)
//                        new_div.appendChild(likes)
//
//                        $('#data').append(new_div)
//
//                        num_para += 1
//
//                    })
//
//                 })
//                 .catch(error => console.error(error))
//          }
//        });


$(document).ready(function(e){

//    alert("document is ready")

//    var request = require('sync-request');
//    var res = http('http://localhost:8000/text/data?paragraph=' + num_para);
//    console.log(res)

    var res = $.ajax("/text/data?paragraph=" + num_para, {
        type: 'GET',
//        async: false,
        success: (response) => {
            console.log(response)
            var data_all = response
            var data = data_all.data
            data.forEach((value, index)=>{
               var number = index + 1
               console.log(number)

               var new_div = document.createElement('div')
               new_div.setAttribute('id', 'paragraph_' + number)

               var p = document.createElement('p')
               p.innerHTML = value.content
               var b = document.createElement('b')
               b.innerHTML = ' (Paragraph: ' + number + ')'
               var likes = document.createElement('button')
               $(likes).attr({'class': ' btn like'})
               $(likes).html('Likes: '+value.likes)

               p.appendChild(b)
               new_div.appendChild(p)
               new_div.appendChild(likes)

               document.getElementById('data').append(new_div)

               num_para += 1
            })

            if (!data_all.next){
                handle_scroll = false
            }

        }})




//    .then(response => response.json())
//    .then(data => {
//        data.data.forEach((value, index)=>{
//           var number = index + 1
//           console.log(number)
//
//           var new_div = document.createElement('div')
//           new_div.setAttribute('id', 'paragraph_' + number)
//
//           var p = document.createElement('p')
//           p.innerHTML = value.content
//           var b = document.createElement('b')
//           b.innerHTML = ' (Paragraph: ' + number + ')'
//           var likes = document.createElement('button')
//           $(likes).attr({'class': ' btn like'})
//           $(likes).html('Likes: '+value.likes)
//
//           p.appendChild(b)
//           new_div.appendChild(p)
//           new_div.appendChild(likes)
//
//           document.getElementById('data').append(new_div)
//
//           num_para += 1
//
//        })

//        if (!data_all.next){
//            handle_scroll = false
//        }

//    });

            fun1();
            fun2();
            fun3();
            fun4();
            fun5();
            fun6();
            fun7();
            fun8();
            fun9();
            fun10();
            fun11();
            fun12();
            fun13();

})


//    // When window loaded ( external resources are loaded too- `css`,`src`, etc...)
//    if (event.target.readyState === "complete") {
//        alert($('#paragraph_1').attr("id"))
//        alert("document is complete")
//
//        window.addEventListener('scroll', () => {
//
//      // Check if we need to handle the scroll event
//      if (!handle_scroll){
//        return
//      }
//      // Get the current scroll position and viewport height
//      const scrollTop = document.documentElement.scrollTop;
//      const windowHeight = window.innerHeight;
//
//      //console.log("scrollTop: ", scrollTop, "windowHeight: ", windowHeight)
//
//      // Get the full document height
//      const fullHeight = document.documentElement.scrollHeight;
//
//      // Check if the user has scrolled to the bottom of the page
//      if (scrollTop + windowHeight >= fullHeight) {
//        // Send a request to your server to fetch more data
//        fetch("http://localhost:8000/text/data?paragraph=" + num_para,
//             {method: 'GET'})
//             .then(response => response.json())
//             .then(data => {
//
//                if (!data.next){
//                    var end_b = document.createElement('b')
//                    $(end_b).text('You have reached the end')
//                    $('#data').after($(end_b))
//                    handle_scroll = false
//                }
//
//                data.data.forEach((value, index)=>{
//
//                    var new_div = document.createElement('div')
//                    new_div.setAttribute('id', 'paragraph_' + value.paragraph)
//                    var p = document.createElement('p')
//                    p.innerHTML = value.content
//                    var b = document.createElement('b')
//                    b.innerHTML = ' (Paragraph: ' + value.paragraph + ')'
//                    var likes = document.createElement('button')
//                    $(likes).attr({'class': ' btn like'})
//                    $(likes).html('Likes: '+value.likes)
//
//                    p.appendChild(b)
//                    new_div.appendChild(p)
//                    new_div.appendChild(likes)
//
//                    $('#data').append(new_div)
//
//                    num_para += 1
//
//                })
//
//             })
//             .catch(error => console.error(error))
//      }
//    });
//    }
//})
//};

//$(document).on('load', function(e){
//    alert('document is loaded')
//})

window.addEventListener('load', function (e) {
//  alert($('#paragraph_1').attr('id'))
//  alert('window is loaded')

})




 window.addEventListener('load', () => {
//  if (document.readyState === 'complete') {
//    var test = document.getElementById('paragraph_1')
//    alert(test.id);
//    alert('Document is fully loaded and rendered');
//  }
//    alert("window is ready")
});



































