
//PAB Create a postJSON function for jQuery, since it doesn't have one.
(function ($) {
    $.postJSON = function (url, data) {
        var o = {
            url: url,
            type: "POST",
            dataType: "json",
            contentType: 'application/json; charset=utf-8'
        };
        if (data !== undefined) {
            o.data = JSON.stringify(data);
        }
        return $.ajax(o);
    };
} (jQuery));

"use strict"

//PAB Create an object gitpatcher
var gitpatcher = gitpatcher || {};

//PAB this warning and error dialogs might be replaceable by jquery-ui componants
gitpatcher.showError = function(message) {
    //PAB Set the modal text
    $("#error-modal .alert").text(message);
    //PAB Display the modal
    $("#error-modal").modal('show');
}

gitpatcher.showWarning = function(message) {
    var messageBox = $("#message-box");
    messageBox.empty();
    $(  '<div class="alert alert-warning alert-dismissible" role="alert">' +
            '<button type="button" class="close" data-dismiss="alert">' +
                '<span aria-hidden="true">&times;</span>' +
                '<span class="sr-only">Close</span>' +
            '</button>' +
            message +
        '</div>').appendTo(messageBox);
}


gitpatcher.cleanResponse = function(data) {
    var delimiter = '\n',
        start     = 0,
        lines     = data.split(delimiter),
        lineCount = lines.length,
        responseLines  = lines.slice(start,lineCount-4),
        response  = responseLines.join(delimiter);
        $(".sqlplus_result").html(response) //Debugging
        //$("#sqlplus-result").val(response);
 
    return JSON.parse(response);                
};

gitpatcher.displaySQLplus = function(data) {

    var responseObj = gitpatcher.cleanResponse(data);
    $("#sqlplus-output").html(responseObj.feedback.output);
    $("#sqlplus-lastline").html(responseObj.feedback.lastLine);
    $("#sqlplus-ans").attr('placeholder',responseObj.feedback.placeholder);
    $("#sqlplus-ans").val('');

    if (responseObj.feedback.ask){
        $("#sqlplus-ans").show();
        $("#sqlplus-next").show();
        $("#sqlplus-done").hide();
        gitpatcher.SQLsessionId = responseObj.sessionId;


    } else {
        $("#sqlplus-ans").hide();
        $("#sqlplus-next").hide();
        $("#sqlplus-done").show();
    }
 
    $("#sqlplus-modal").modal('show');
 
    return;                
};


//PAB attempt to contact db via sqlplus and show a result.
gitpatcher.refreshRepoList = function() {
    
    //$.getJSON("/getrepolist", function(result){
    //    return result;
    //});
    
//Lets try to call the server..    
$.postJSON('/repolist', {param1: "hello", param2: "world"})
    .complete(function (data) {
        // Optional - fires when the operation completes, regardless of status
        return data;
    })
    .success(function (data) {
        // Optional - fires when operation completes successfully
        return data;
    })
    .error(function (data) {
        // Optional - fires when operation completes with error
        return data;
    });
    
 
    
    //return "result";
//$("#post-result").html('Pushed');
/*
    $.post("refreshRepoList", query, function(data, status, xhr) { //Calls new routine
        if (xhr.status == 200) {
 
            //gitpatcher.displaySQLplus(data);
    
            $("#post-result").html(data); //PAB write the result data to display item.
       
        } else {
            console.log(data);
            gitpatcher.showError(data);
        }
    }, "text")
    .fail(function(xhr, status, error) {
        gitpatcher.showError("SQLplus Error: " + error);
    });
*/    
};