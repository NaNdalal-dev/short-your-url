
      copyTextBtn = document.getElementById('copyTextBtn');
      alert(copyTextBtn)
      copyTextBtn.addEventListener('click', function(event) {
        let copyTextarea = document.querySelector('#copytextarea');
        copyTextarea.focus();
        copyTextarea.select();
        try {
          let successful = document.execCommand('copy');
          let msg = successful ? 'successful' : 'unsuccessful';
          alert('Copy text command was ' + msg);
        } catch(err) {
          alert('Unable to copy');
        }
      });