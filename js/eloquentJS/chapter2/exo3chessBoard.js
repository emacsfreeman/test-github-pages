// Version 1 : for the chessBoard
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

// Version 2 : for any grid
let length = 6;
let width = 12;
for (let x = 0; x < length; x++) 
{
    let string = "";
    for (let y = 0; y < width; y++) 
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
