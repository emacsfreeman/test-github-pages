let size = 8;
for (let x = 0; x < size; x++) 
{
    let string = "";
    for (let y = 0; y < size; y++) 
    {
        if ((x + y) % 2 == 0) 
        {
            string += " ";
        }
        else if ((x + y) % 2 == 1)
        {
            string += "#";
        }
    }
    console.log(string + "\n");
}
