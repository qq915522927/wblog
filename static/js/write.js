/**
 * Created by 91552 on 2017-07-24.
 */

function get_classify(uid) {
    var response = $('.list_classify');
    response.html('');
    $.get('/api/classify?u='+uid,function (data) {
        l = data.data;
        for(index in l){
            var title = l[index]['title'];
            var id = l[index]['id'];
            var content= '\<li\><a href="javascript:get_posts('+id+'\)">'+title+'\</a>\<a href="/del_classify/'+id+'\" class=\"del_classify\"\>删除\</a></li>';
            response.append(content);
        }
    })

}
function get_posts(c) {
    var response = $('.write_m');
    response.html('');

    $.get('/api/posts/'+c,function (data) {

        l = data.data;
        simplemde.value(l[0].body);
        $('.text_pid').val(l[0].id);
        for(index in l){
            var title = l[index]['title'];
            var id = l[index]['id'];
            var content =  '\<div class="post_list"><a href="javascript:get_post( '+id+'\)\" class=\"title\"\>'+title+'\</a><a class="del_post/'+id+'\"\>删除</a></div>';
            response.append(content);
        }

    })

}
function get_post(id) {
    $.get('/api/post/'+id,function (data) {
        simplemde.value(data.body);
         $('.text_pid').val(data.id);

    })

}