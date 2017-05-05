
$(function(){
    $("form[name='addEventForm']").validate({
        rules:{
            Event_Name:"required",
            Event_Date:"required",
            Event_Info:"required",
            Event_Place:"required"
        },

        messages:{
            Event_Name:"Please enter the event name",
            Event_Date:"Please enter the event date",
            Event_Info:"Please enter the event information",
            Event_Place:"Please enter the event place"
        },

        submitHandler:function(form){
            form.submit();
        }

    });
});
