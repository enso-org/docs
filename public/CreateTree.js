$.fn.extend({
    treed: function(o) {

        var openedClass = 'fa fa-caret-down';
        var closedClass = 'fa fa-caret-right';

        if (typeof o != 'undefined') {
            if (typeof o.openedClass != 'undefined') {
                openedClass = o.openedClass;
            }
            if (typeof o.closedClass != 'undefined') {
                closedClass = o.closedClass;
            }
        };

        //initialize each of the top levels
        var tree = $(this);
        tree.addClass("treeMenu");
        tree.find('li').has("ul").each(function() {
            var branch = $(this); //li with children ul
            branch.prepend("<i class='indicator glyphicon " + closedClass + "'></i>");
            branch.addClass('branch');
            branch.on('click', function(e) {
                if (this == e.target) {
                    var icon = $(this).children('i:first');
                    icon.toggleClass(openedClass + " " + closedClass);
                    $(this).children().children().toggle();
                }
            })
            branch.children().children().toggle();
        });
        //fire event from the dynamically added icon
        tree.find('.branch .indicator').each(function() {
            $(this).on('click', function() {
                $(this).closest('li').click();
            });
        });

        //fire event to open branch if the li contains a button instead of text
        tree.find('.branch>button').each(function() {
            $(this).on('click', function(e) {
                $(this).closest('li').click();
            });
        });
    }
});

//Initialization of treeviews
MutationObserver = window.MutationObserver || window.WebKitMutationObserver;

// define a new observer
var obs = new MutationObserver(function(mutations, observer) {
    // look through all mutations that just occured
    for (var i = 0; i < mutations.length; ++i) {
        // look through all added nodes of this mutation
        for (var j = 0; j < mutations[i].addedNodes.length; ++j) {
            // was a child added with ID of 'bar'?
            if (mutations[i].addedNodes[j].id == "treeMID") {
                $('#treeMID').treed();

                $(function() {
                    // this will get the full URL at the address bar
                    var url = window.location.href;

                    // passes on every "a" tag
                    $(".treeMenu a").each(function() {
                        // checks if its the same on the address bar
                        if (url == (this.href)) {
                            $(this).closest("a").addClass("active");
                            //for making parent of submenu active
                            $(this).closest("a").parent().parent().parent().addClass("active");
                            $(this).closest("a").parent().parent().parent().children().addClass("active");
                            $(this).closest("a").parent().parent().parent().parent().parent().addClass("active");
                            $(this).closest("a").parent().parent().parent().parent().parent().children().addClass("active");
                        }
                    });
                });
            }
        }
    }
});

// have the observer observe for changes in children
obs.observe($("#menuPane").get(0), {
    childList: true
});