document.addEventListener('DOMContentLoaded', function() {
    const sliders = document.querySelectorAll('.slideDiv');
    console.log(sliders)
    const blanquiOptions = {
        threshold: 1
    }
    const blanquiObserver = new IntersectionObserver
    (function(
        entries, 
        blanquiObserver
    ) {
        entries.forEach(entry => {
            if(!entry.isIntersecting){
                return;
            } else{
                entry.target.classList.add('slide-in');
                blanquiObserver.unobserve(entry.target);
            }
        })
    }, 
    blanquiOptions);
    
    sliders.forEach(slider => {
        blanquiObserver.observe(slider);
    })

    const slider2 = document.querySelector('.gerald_div');
    console.log(slider2)
    const geraldOptions = {
        threshold: 1
    }
    const geraldObserver = new IntersectionObserver
    (function(
        entries, 
        geraldObserver
    ) {
        entries.forEach(entry => {
            if(!entry.isIntersecting){
                return;
            } else{
                entry.target.classList.add('slide-in2');
                geraldObserver.unobserve(entry.target);
            }
        })
    }, 
    geraldOptions);
    
    geraldObserver.observe(slider2);

})
