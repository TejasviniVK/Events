/**
 * Created by cfit001 on 1/3/17.
 */
function CheckPlace(val) {
    if (val == 'other')
        $("#textbox_place").show();
    else
        $("#textbox_place").hide()
}


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function ajaxsetup() {
    var csrftoken = getCookie('csrftoken');
    $.ajaxSetup({
        beforeSend: function (xhr) {
            if (!this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

}

$(document).ready(function () {

    $("#selectevent").select2();


    $('#addeventbutton').click(function () {

        ajaxsetup();


        var regex = /^[A-Za-z0-9]/;
        var nameValue = $('#name_textbox').val();
        var infoValue = $('#info_textbox').val();
        var dateValue = $('#date_textbox').val();
        var placeValue = $('#selectplace').val();
        var newPlace = $('#textbox_place').val();

        if (regex.test(nameValue) && dateValue != '' && placeValue != '' && regex.test(infoValue)) {


            $.ajax({

                type: "POST",

                url: '/add_event',

                data: {
                    'Event_Name': nameValue,
                    'Event_Info': infoValue,
                    'Event_Date': dateValue,
                    'Event_Place': placeValue,
                    'new_place': newPlace
                },

                success: function (data) {

                    $('#successmsg').html(data)
                },

                error: function () {
                    $('#successmsg').text('Name already exists.Give another name')
                }


            });


        }


        else {
            $('#successmsg').text("All Fields must be filled properly")
        }


    });


    $('#searcheventbutton').click(function () {

        ajaxsetup();

        var searchEventName = $('#selectevent').val();

        if (searchEventName == '') {
            $('#searchsuccessmsg').text("Search Failed")
        }

        else {

            $.ajax({

                type: "POST",


                url: '/search_event',


                data: {'search_ID': searchEventName},


                success: function (data) {

                    $('#searchsuccessmsg').html(data);

                },


                error: function () {

                    $('#searchsuccessmsg').text("Some issue occured")

                }

            });

        }


    });

    $('#datebutton').click(function () {

        ajaxsetup();

        var dateValue1 = $('#datevalue').val();

        if (dateValue1 == '') {

            $('#datesuccessmsg').text("Please enter a valid date")

        }

        else {

            $.ajax({

                type: "POST",

                url: '/list_by_date',

                data: {'Date_Search': dateValue1},

                success: function (data) {

                    $('#datesuccessmsg').html(data);
                    tableculture();

                },

                error: function () {
                    $('#datesuccessmsg').text("Some issue occured!! ")
                }


            });
        }

    });


    $('#dateplacebutton').click(function () {

        ajaxsetup();

        var datePlaceValue1 = $('#dateplacevalue').val();

        var selectPlace12 = $('#selectplace1').val();

        if (datePlaceValue1 == '' || selectPlace12 == '') {

            $('#dateplacesuccessmsg').text("Please enter a valid date and place ")

        }

        else {

            $.ajax({

                type: "POST",

                url: '/list_by_date_place',

                data: {'Date_Place': datePlaceValue1, 'Place_Date': selectPlace12},

                success: function (data) {

                    $('#dateplacesuccessmsg').html(data);
                    tableculture();
                },

                error: function () {
                    $('#dateplacesuccessmsg').text("Some issue occured!! ")
                }

            });

        }

    });

    $('#placebutton').click(function () {

        ajaxsetup();

        var selectPlace31 = $('#selectplace3').val();


        if (selectPlace31 == '') {

            $('#placesuccessmsg').text("Please enter a valid place ")

        }

        else {

            $.ajax({

                type: "POST",

                url: '/list_by_place',

                data: {'Place_Search': selectPlace31},

                success: function (data) {

                    $('#placesuccessmsg').html(data);
                    tableculture();
                },

                error: function () {
                    $('#placesuccessmsg').text("Some issue occured!! ")
                }


            });
        }
        tableculture();
    });


    $('#rangebydatebutton').click(function () {

        ajaxsetup();

        var date12 = $('#date1').val();

        var date22 = $('#date2').val();


        if (date12 == '' || date22 == '') {

            $('#daterangesuccessmsg').text("Please fill in both the fields ")

        }


        else {

            $.ajax({

                type: "POST",

                url: '/range_by_date',

                data: {'Date1': date12, 'Date2': date22},


                success: function (data) {

                    $('#daterangesuccessmsg').html(data);
                    tableculture();
                },

                error: function () {
                    $('#daterangesuccessmsg').text("Some issue occured!!! ")
                }


            });
        }

    });


    tablecultureforevents();



});


function updateevent() {

    ajaxsetup();

    var regex1 = /^[A-Za-z0-9]/;
    var hidd = $('#hiddenID').val();
    var name_update = $('#name').val();
    var place_update = $('#place').val();
    var date_update = $('#date').val();
    var info_update = $('#info').val();

    if (regex1.test(name_update) && date_update != '' && place_update != '' && regex1.test(info_update)) {
        $.ajax({
            type: "POST",

            url: '/update_event',

            data: {
                'search_ID': hidd,
                'Event_Name': name_update,
                'Event_Date': date_update,
                'Event_Place': place_update,
                'Event_Info': info_update
            },

            success: function (data) {
                $('#searchsuccessmsg').slideUp('slow');
                $('#msg').text(data);
                setTimeout(function () {location.reload();}, 5000);
            },

            error: function () {
                $('#msg').text("some error occured!")
            }
        });
    }

    else {
        $('#msg').text("Please enter updated fields properly!!")
    }

}


function deleteevent() {
    ajaxsetup();

    var hiddenDelete = $('#hiddenID').val();


    $.ajax({

        type: "POST",

        url: '/del_event',

        data: {'search_ID': hiddenDelete},

        success: function (data) {
            $('#searchsuccessmsg').slideUp('slow');
            $('#msg').text(data)
        },

        error: function () {
            $('#msg').text("some error occured!")
        }


    });


}


function tableculture() {
    $('#tableforfilter').table_scroll({

        rowsInHeader: null,

        rowsInFooter: null,

        fixedColumnsLeft: 0,
        fixedColumnsRight: 0,
        scrollX: 0,

        scrollY: 0,
        rowsInScrollableArea: 4,
        columnsInScrollableArea: 4,

        overflowY: 'scroll',

        overflowX: 'auto'


    });


}


function tablecultureforevents(){
  $('#tableforevents').table_scroll({

        rowsInHeader: null,

        rowsInFooter: null,

        fixedColumnsLeft: 0,
        fixedColumnsRight: 0,
        scrollX: 0,

        scrollY: 0,
        rowsInScrollableArea: 10,
        columnsInScrollableArea: 10,

        overflowY: 'scroll',

        overflowX: 'auto'


    });


}









