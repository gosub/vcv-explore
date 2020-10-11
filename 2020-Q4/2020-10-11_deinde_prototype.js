
config.frameDivider = 1
config.bufferSize = 32

function clamp(value, min, max) {
    if (value < min) {
        return min;
    } else if (value > max) {
        return max;
    } else {
        return value;
    }
}

function process(block) {
    for (let buff_idx = 0; buff_idx < block.bufferSize; buff_idx++) {
        let input = block.knobs[0] * 10;
        output0 = clamp(input * 4, 0, 10);
        output1 = clamp(input * 4 - 10, 0, 10);
        output2 = clamp(input * 4 - 20, 0, 10);
        output3 = clamp(input * 4 - 30, 0, 10);


        block.outputs[0][buff_idx] = output0;
        block.outputs[1][buff_idx] = output1;
        block.outputs[2][buff_idx] = output2;
        block.outputs[3][buff_idx] = output3;
    }
}
