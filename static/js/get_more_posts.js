$('.post-btn').click(function(){
  $.ajax({
  　url: 'get_more_posts',
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
  　url: 'get_more_posts',
  　type: 'get',
  　cache: false,
  　dataType:'html'
  　})
    
  　.done(function(response) {
      $('.load-btn').before(response);
  　})

  　.fail(function(data) {
      window.alert("failed");
  　})
});
