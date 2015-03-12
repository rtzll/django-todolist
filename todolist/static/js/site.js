$(document).ready(function() {

  // Variables
  var $nav = $('.navbar'),
      $body = $('body'),
      $window = $(window),
      $popoverLink = $('[data-popover]'),
      navOffsetTop = $nav.offset().top,
      $document = $(document);

  function init() {
    $window.on('scroll', onScroll);
    $window.on('resize', resize);
    $popoverLink.on('click', openPopover);
    $document.on('click', closePopover);
    $('a[href^="#"]').on('click', smoothScroll);
    $('input[type=text]:first').focus();
    $('input[type=text]:first').on('keypress click', function() {
        $('.has-error').hide();
    });
  }

  function smoothScroll(e) {
    e.preventDefault();
    $(document).off("scroll");
    var target = this.hash,
        menu = target;
    $target = $(target);
    $('html, body').stop().animate({
        'scrollTop': $target.offset().top-40
    }, 0, 'swing', function () {
        window.location.hash = target;
        $(document).on("scroll", onScroll);
    });
  }

  function openPopover(e) {
    e.preventDefault();
    closePopover();
    var popover = $($(this).data('popover'));
    popover.toggleClass('open');
    e.stopImmediatePropagation();
  }

  function closePopover(e) {
    if($('.popover.open').length > 0) {
      $('.popover').removeClass('open');
    }
  }

  $('#button').click(function() {
    $('html, body').animate({
        scrollTop: $('#elementtoScrollToID').offset().top
    }, 2000);
  });

  function resize() {
    $body.removeClass('has-docked-nav');
    navOffsetTop = $nav.offset().top;
    onScroll();
  }

  function onScroll() {
    if(navOffsetTop < $window.scrollTop() &&
      !$body.hasClass('has-docked-nav')) {
      $body.addClass('has-docked-nav')
    }
    if(navOffsetTop > $window.scrollTop() &&
      $body.hasClass('has-docked-nav')) {
      $body.removeClass('has-docked-nav')
    }
  }


  $(':checkbox').on('click', changeTodoStatus);

  function changeTodoStatus() {
    if($(this).is(':checked')) {
      putNewStatus(this.getAttribute('data-todo-id'), true);
    } else {
      putNewStatus(this.getAttribute('data-todo-id'), false);
    }
  }

  function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }

  function putNewStatus(todoID, isFinished) {

    // setup ajax to csrf token
    var csrftoken = getCookie('csrftoken');
    $.ajaxSetup({
      beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
          xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
      }
    });
    // send put request using the data of the get for the same id
    var todoURL = '/api/todos/' + todoID + '/'
    $.getJSON(todoURL, function(data) {
      data.is_finished = isFinished;
      if (isFinished) {
        data.finished_at = moment().toISOString();
      }
      console.log(JSON.stringify(data));
      $.ajax({
        url: todoURL,
        type: 'PUT',
        contentType: 'application/json',
        data: data,
        success: function() {
          location.reload();
        }
      });
    });
  }

  // function from the django docs
  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(
                  cookie.substring(name.length + 1)
                );
                break;
            }
        }
    }
    return cookieValue;
  }

  init();

});