function block(el) {

  var block_ele = $(el);

  // Block Element
  block_ele.block({
    message: '<div class="spinner-border text-primary" role="status">\n' +
      '  <span class="sr-only"></span>\n' +
      '</div>',
    overlayCSS: {
      backgroundColor: "#fff",
      cursor: "wait"
    },
    css: {
      border: 0,
      padding: 0,
      backgroundColor: "none"
    }
  });
}


function unblock(el) {
  $(el).unblock();
}

var $csrf_token = $('[name="csrfmiddlewaretoken"]').attr('value');


$('#contact__form').submit(function (e) {
  e.preventDefault();

  let name = $("[name=name]")
  let phoneNumberInput = $("[name=phone_number]")
  let message = $("[name=message]")

  const phoneRegex = new RegExp("^(\\+98|0)?9\\d{9}$");
  const phoneNumber = phoneNumberInput.val().trim();

  if (name.val() === null && name.val().length >= 25 && name.val().length <= 3) {
    name.addClass("is_invalid");
    document.querySelector('#errorName').classList.remove('d-none')
    document.querySelector('#errorName').textContent = "نام خود را وارد کنید.(نمی تواند بیش از 25 و کمتر از 3 کاراکتر باشد)"
  } else {
    name.removeClass("is_invalid");
    document.querySelector('#errorName').classList.add('d-none')
  }

  if (phoneRegex.test(phoneNumber)) {
    // remove error style and set to default:
    phoneNumberInput.removeClass("is_invalid");
    document.querySelector('#errorPhone').classList.add('d-none')
  } else {
    // style for error:
    phoneNumberInput.addClass("is_invalid");
    document.querySelector('#errorPhone').classList.remove('d-none')
    document.querySelector('#errorPhone').textContent = "شماره تلفن باید بصورت (09123334455) وارد شود."
  }

  if (message.val() === null && message.val().length >= 1000 && message.val().length <= 10) {
    message.addClass("is_invalid");
    document.querySelector('#errorMessage').classList.remove('d-none')
    document.querySelector('#errorMessage').textContent = "پیام خود را وارد کنید.(نمی تواند بیش از 1000 و کمتر از 10 کاراکتر باشد)"
  } else {
    message.removeClass("is_invalid");
    document.querySelector('#errorMessage').classList.add('d-none')
  }

  if (
    name.val() !== null && name.val().length <= 25 && name.val().length >= 3
    && phoneRegex.test(phoneNumber)
    && message.val() !== null && message.val().length <= 1000 && message.val().length >= 10
  ) {
    $.ajax({
      method: "POST",
      url: '/api/contact/',
      data: JSON.stringify({
        name: name.val(),
        phone_number: phoneNumberInput.val().trim(),
        message: message.val()
      }),
      headers: {"X-CSRFToken": $csrf_token},
      contentType: "application/json",
      processData: false,
      beforeSend: function (xhr) {
        block('#contact__form')
      },
      complete: function () {
        unblock('#contact__form')
      },
      success: function () {
        toastr.success('کارشناسان ما در اسراء وقت با شما تماس میگیرند', 'پیام شما با موفقیت ثبت شد', {timeOut: 5000})
        toastr.options.progressBar = true;
        toastr.options.rtl = true;
        document.querySelector('.youre_name').value = '';
        document.querySelector('.phone_number').value = '';
        document.querySelector('.message').value = '';
      },
      error: function () {
        toastr.error('خطایی رخ داده است.', {timeOut: 5000})
        toastr.options.progressBar = true;
        toastr.options.rtl = true;
      }
    })
  } else {
    toastr.error('خطایی رخ داده است.', {timeOut: 5000})
    toastr.options.progressBar = true;
    toastr.options.rtl = true;
  }
})


$('#Subscribe__form').submit(function (e) {
  e.preventDefault();

  let email = $("[name=email]")

  if (email.val() === null) {
    email.addClass("is_invalid");
    document.querySelector('#errorEmail').classList.remove('d-none')
    document.querySelector('#errorEmail').textContent = "ایمیل خود را وارد کنید.(نمی تواند بیش از 1000 و کمتر از 10 کاراکتر باشد)"
  } else {
    email.removeClass("is_invalid");
    document.querySelector('#errorEmail').classList.add('d-none')
  }

  if (email.val() !== null) {
    $.ajax({
      method: "POST",
      url: '/api/newsletter/subscribe/',
      data: JSON.stringify({
        email: email.val(),
      }),
      headers: {"X-CSRFToken": $csrf_token},
      contentType: "application/json",
      processData: false,
      beforeSend: function (xhr) {
        block('#Subscribe__form')
      },
      complete: function () {
        unblock('#Subscribe__form')
      },
      success: function () {
        toastr.success('شما از این پس از جدید ترین اخبار و پیشنهادات ما باخبر خواهید شد.', 'ایمیل شما با موفقیت ثبت شد', {timeOut: 5000})
        toastr.options.progressBar = true;
        toastr.options.rtl = true;
        document.querySelector('#subscribe-email').value = '';
      },
      error: function () {
        toastr.error('خطایی رخ داده است.', {timeOut: 5000})
        toastr.options.progressBar = true;
        toastr.options.rtl = true;
      }
    })
  } else {
    toastr.error('خطایی رخ داده است.', {timeOut: 5000})
    toastr.options.progressBar = true;
    toastr.options.rtl = true;
  }
})