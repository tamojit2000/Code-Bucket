Array.prototype.forEach.call(document.querySelectorAll('.file-upload__button'),function(button)
{
    const hiddenInput=button.parentElement.querySelector('.file-upload__input');
    const label=button.parentElement.querySelector('.file-upload__label');
    const defaultLabelText='No file selected';

    //Set default text for upload__label

    label.textContent = defaultLabelText;
    label.title = defaultLabelText;

    button.addEventListener('click',function()
    {
        hiddenInput.click();
    });
    hiddenInput.addEventListener('change',function()
    {
        console.log(hiddenInput.files);
        const filenameList=Array.prototype.map.call(hiddenInput.files,function(file)
        {
            return file.name;
        });
        label.textContent = filenameList.join()||defaultLabelText;
        label.title= label.textContent;
    })
});
const realFileBtn=document.getElementById("real-file");
const customBtn=document.getElementById("custom-button");
customBtn.addEventListener("click",function()
{
    realFileBtn.click();
});
