window.addEventListener("DOMContentLoaded", () => {
  const switch_btn = document.getElementById("settings_btn");
  const search_field = document.getElementById("settings_field");
  
  switch_btn.addEventListener("click", () => {
    if(getComputedStyle(search_field).display == "none"){
      search_field.style.display = "flex";
    } else {
      search_field.style.display = "none";
    }
  })
})

window.addEventListener("DOMContentLoaded", () => {
  const switch_btn = document.getElementById("skypech_btn");
  const search_field = document.getElementById("skypech_field");
  
  switch_btn.addEventListener("click", () => {
    if(getComputedStyle(search_field).display == "none"){
      search_field.style.display = "flex";
    } else {
      search_field.style.display = "none";
    }
  })
})
