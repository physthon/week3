var simplemde = new SimpleMDE({
    element: document.getElementById("area_mde"),
    autofocus: true,
    autosave: {
      enabled: true,
      uniqueId: "area_mde",
      delay: 1000,
    },
    previewRender: function(plainText, preview) {
      setTimeout(function() {
        markjax(plainText, preview);
      }, 50);
      return preview.innerHTML;
    },
  });
  