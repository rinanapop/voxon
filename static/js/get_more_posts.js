$('.post-btn').click(function(){
  $.ajax({
  　url: 'skypech',
  　type: 'post',
  　cache: false,
  　dataType:'html',
    data:{ id: $(this).attr('id')}
  　})
    
  　.done(function(response) {
      $('#master').html(response);
  　})

  　.fail(function(data) {
      window.alert("failed");
  　})
});

$('.load-btn').click(function(){
  $.ajax({
  　url: 'skypech',
  　type: 'get',
  　cache: false,
  　dataType:'html'
  　})
    
  　.done(function(response) {
      $('.field').append(response);
  　})

  　.fail(function(data) {
      window.alert("load failed");
  　})
});

$('.reload-btn').click(function(){
  $.ajax({
  　url: 'skypech',
  　type: 'get',
  　cache: false,
  　dataType:'html'
  　})
    
  　.done(function(response) {
      $('.field').html(response);
  　})

  　.fail(function(data) {
      window.alert("reload failed");
  　})
});

$('.clear-btn').click(function(){
  $('.field').empty();
});
