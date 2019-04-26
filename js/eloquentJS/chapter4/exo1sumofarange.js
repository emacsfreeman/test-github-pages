function range(start, end)
{
    let result = [];
    result.push(start);
    for (let i = 1; i < end - start + 1; i++)
    {
        result.push(start + i);
    }
    return result;
}

// Test
console.log(range(1, 10));
console.log(range(2, 5));

function sum(tab)
{
    let result = 0;
    for (let i = 0; i < tab.length; i++)
    {
        result += tab[i];
    }
    return result;
}

// Test 
console.log(sum(range(1, 10)));

function rangeBonus(start, end, step = 1)
{
    let result = [];
    for (let i = 0; i < end - start + 1; i += step)
    {
        result.push(start + i);
    }
    return result;
}

// Test 
console.log(sum(rangeBonus(1, 10)));
console.log(sum(rangeBonus(1, 10, 2)));
