function max_3 (num1, num2, num3) {
    // program to find the largest among three numbers

    let largest

    // check the condition
    if(num1 >= num2 && num1 >= num3) {
        largest = num1
    }
    else if (num2 >= num1 && num2 >= num3) {
        largest = num2
    }
    else {
        largest = num3
    }

    return largest
}
