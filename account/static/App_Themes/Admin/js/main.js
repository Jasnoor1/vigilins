/*
Author: Priyaranjan Rout
Description: Custom js
Version: 1.0
Contact: ranjanpriya92@gmail.com / +91-9853759434 / priyaranjan.rout@emtpl.com
*/

// --- Left Menu JS
$(document).on('click', '#LeftSidemenu.SideMenu  li  a', function () {
    if ($(this).siblings('ul').hasClass('ChildMenu')) {
        $(this).siblings('ul').toggle(1000);
        $(this).siblings('ul').toggleClass('active');
        $(this).parent('li').siblings('li').children('ul').hide();
        $(this).parent('li').siblings('li').children('ul').removeClass('active');
    }
    else {
        $('ul.ChildMenu').hide();
        $('ul.ChildMenu').removeClass('active');
    }
});

// --- Top Menu Right
$(document).on('click', '.TopHeaderRight > li a.nav-link', function () {
    if ($(this).siblings('div').hasClass('dropdown-menu')) {
        $(this).siblings('div.dropdown-menu').toggle(1000);
        $(this).parent('li').siblings('li').children('div.dropdown-menu').hide();
    }
    else {
        $('div.dropdown-menu').hide();
    }
});

// Top toggle for left menu
$(document).on('click', '.TopHeader .TopHeaderLeft .MenuToggle', function () {
    $('body').toggleClass('SmallLeftMenu')
});

// --- On body Click
$(document).on('click', 'body', function (e) {
    if ($(e.target).closest("#LeftSidemenu.SideMenu  li").length > 0) {
        //return false;
    }
    else {
        $('ul.ChildMenu').removeClass('active');
        $('ul.ChildMenu').hide();
    }
});

// Cards
$(document).on('click', '.card .card-header .ToggleCardBody', function () {
    $(this).parents('.card-header').siblings('.card-body').toggle(500);
    $(this).toggleClass('active')
});

//Document Ready
$(document).ready(function () {
    //Tooltip
    $('[data-toggle="tooltip"]').tooltip();
});