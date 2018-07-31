$(function () {
    fp();
    minus();
});

function fp(obj) {
    let num = $(obj).next().val();
    let t = $(obj).parent().parent().next().find("span").html();
    let pri = $(obj).parent().parent().prev().html();
    let name = $(obj).parent().parent().prev().prev().prev().prev().children().attr("src");
    if (num >= 100) {
        num = 100;
        $(obj).next().val(num);
        let s = 100 * parseFloat(pri);
        $(obj).parent().parent().next().find("span").html(s.toFixed(2))
    } else {
        num++;
        $.ajax({
            type: 'POST',
            url: "{% url 'user:cart_update' %}",
            data: {"num": num, "p_name": name, crsvmiddletoken: "csrf_token"},
            dataType: "json",

        });
        $(obj).next().val(num);
        let s = num * parseFloat(pri);
        $(obj).parent().parent().next().find("span").html(s.toFixed(2));


    }
}

function minus(obj) {
    let num = $(obj).prev().val();
    let t = $(obj).parent().parent().next().find("span").html();
    let pri = $(obj).parent().parent().prev().html();
    let name = $(obj).parent().parent().prev().prev().prev().prev().children().attr("src");
    if (num <= 1) {
        num = 1;
        $(obj).prev().val(num);
        let s = num * parseFloat(pri);
        $(obj).parent().parent().next().find("span").html(s.toFixed(2))
    } else {
        num--;
        alert(num);
        alert(name);
        $.ajax({
            type: 'POST',
            url: "{% url 'user:cart_update' %}",
            data: {"num": num, "p_name": name, crsvmiddletoken: "csrf_token"},
            dataType: "json",

        });
        $(obj).prev().val(num);
        let s = num * parseFloat(pri);
        $(obj).parent().parent().next().find("span").html(s.toFixed(2))

    }
};