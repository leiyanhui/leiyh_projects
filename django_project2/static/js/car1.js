function allchoose(obj) {
    $(".choose_box").each(function (i) {
        if ($(obj).is(":checked") === false) {
            $(this).prop("checked", false);
            $("#num_checked").html(0);
        } else {
            $(this).prop("checked", true);
            let total_count = $("#total_count").html();
            $("#num_checked").html(total_count);
        }
    });
}

function choose() {
    let num = 0;
    let count = 0;
    if ($("#allchoose").is(":checked") === true) {
        $(".choose_box").each(function (i) {
            if ($(this).is(":checked") === false) {
                $("#allchoose").prop("checked", false);
                return false;
            } else {
                count++;

            }
        });
        $("#num_checked").html(count)
    } else {
        $(".choose_box").each(function (i) {
            if ($(this).is(":checked") === true) {
                num++;

            }
        });
        if ($(".choose_box").length === num) {
            $("#allchoose").prop("checked", true);
        }
        $("#num_checked").html(num)
    }

}

