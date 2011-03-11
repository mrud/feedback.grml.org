function prettify_feedback(feedback) {
  var errorLog = null;
  var feedbackInput = null;
  var errors = 0;

  function showFormError(error) {
    if (errorLog === null) {
      errorLog = $('<p class=error></p>').insertAfter('.feedback p.version');
      errorLog.hide().slideDown();
    }
    errorLog.text(error);
  }

  function clearErrorLog() {
    if (errorLog) {
      errorLog.slideUp();
      errorLog.text('');
    }
  }

  function updateCharsLeft() {
    var delta = $('[name="feedback"]', feedback).attr('maxlength') - feedbackInput.val().length;
    charsLeft.text('' + delta);
    charsLeft.toggleClass('chars-over-limit', delta < 0);
    if (!charsLeft.is(':visible'))
      charsLeft.fadeIn('slow');
  }

  function prepareEntry(kind) {
    return function() {
      $('select[name="kind"]').val(kind);
      $('.kind-selector', feedback).removeClass('active-kind');
      $(this).parent().addClass('active-kind');
      $($("li", $('.feedback'))[1]).show()
        $('[name="feedback"]').val("");
    }
  }

  feedbackInput = $('[name="feedback"]', feedback).keyup(function() {
    updateCharsLeft();
    var nextStep = $('.step2', feedback);
    if (this.value.length >= 10)
    nextStep.slideDown('fast');
    else
    nextStep.slideUp('fast');
  });

  function validateVersion(elem) {
    if (elem.value.length > 0 && ! elem.value.match(/^(\d{4}\.\d{2})|(daily)$/)) {
      showFormError('Wrong version. Use YEAR.MONTH (2010.12) or daily');
      return false;
    } else {
      clearErrorLog();
      return true;
    }
  }
  $('input[name="version"]').keyup(function() { validateVersion(this); });
  charsLeft = $('<span class=chars-left></span>')
    .insertBefore(feedbackInput)
    .hide();

  feedback.bind('submit', function() {
    if  ($('input[name="version"]') &&
      ! validateVersion($('input[name="version"]')[0]))
    {
      showFormError('Wrong version. Use YEAR.MONTH (2010.12) or daily')
      return false;
    }
    if ($("#chars-over-limit").length) {
      showFormError('Message too long :/')
      return false;
    }
  });
  $('select[name="kind"]').hide();
  $('.selectors').append('<span class="kind-selector"><a href=# class=happy>happy ☺</a></span> / <span class="kind-selector"><a href=# class=unhappy>unhappy ☹</a></span>');
  $('a.happy', feedback).click(prepareEntry('h'));
  $('a.unhappy', feedback).click(prepareEntry('u'));


}

$(function() {
  var feedback = $('.feedback');
  $('.hide').hide()
  prettify_feedback(feedback);
})
