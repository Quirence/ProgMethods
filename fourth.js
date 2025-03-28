const fs = require("fs");

const SAMPLE_RATE = 10000;
const DURATION = 1; // in seconds
const N = SAMPLE_RATE * DURATION; // Number of samples

// Generate signal
function generateSignal(frequencies, amplitudes) {
    let signal = new Array(N).fill(0);
    for (let i = 0; i < N; i++) {
        let t = i / SAMPLE_RATE;
        for (let j = 0; j < frequencies.length; j++) {
            signal[i] += amplitudes[j] * Math.cos(2 * Math.PI * frequencies[j] * t);
        }
    }
    return signal;
}

// Compute Discrete Fourier Transform (DFT)
function dft(signal) {
    let frequencies = [], amplitudes = [];
    for (let k = 0; k < N / 2; k++) {
        let real = 0, imag = 0;
        for (let n = 0; n < N; n++) {
            let angle = (2 * Math.PI * k * n) / N;
            real += signal[n] * Math.cos(angle);
            imag -= signal[n] * Math.sin(angle);
        }
        let amplitude = Math.sqrt(real * real + imag * imag) / N;
        frequencies.push((k * SAMPLE_RATE) / N);
        amplitudes.push(amplitude);
    }
    return { frequencies, amplitudes };
}

// Save data to CSV for Excel visualization
function saveToCSV(frequencies, amplitudes, filename) {
    let csvContent = "Frequency,Amplitude\n";
    for (let i = 0; i < frequencies.length; i++) {
        csvContent += `${frequencies[i]},${amplitudes[i]}\n`;
    }
    fs.writeFileSync(filename, csvContent);
}

// Generate and process signals
let testCases = [
    { f: [100], a: [1] },
    { f: [100, 300, 700], a: [1, 1, 1] },
    { f: [100, 300, 700], a: [3, 2, 1] }
];

testCases.forEach((testCase, index) => {
    let signal = generateSignal(testCase.f, testCase.a);
    let { frequencies, amplitudes } = dft(signal);
    saveToCSV(frequencies, amplitudes, `dft_result_${index + 1}.csv`);
    console.log(`Saved DFT results for case ${index + 1} to dft_result_${index + 1}.csv`);
});
