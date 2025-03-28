const SAMPLE_RATE = 10000;
const DURATION = 1;
const N = SAMPLE_RATE * DURATION;

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

function dft(signal) {
    let halfN = Math.floor(N / 2);
    let amplitudes = new Array(halfN).fill(0);
    let frequencies = new Array(halfN);

    for (let k = 0; k < halfN; k++) {
        let real = 0, imag = 0;
        for (let n = 0; n < N; n++) {
            let angle = (2 * Math.PI * k * n) / N;
            real += signal[n] * Math.cos(angle);
            imag -= signal[n] * Math.sin(angle);
        }
        amplitudes[k] = Math.sqrt(real * real + imag * imag) / N;
        frequencies[k] = k * SAMPLE_RATE / N;
    }
    return { frequencies, amplitudes };
}

function printForExcel(frequencies, amplitudes) {
    console.log("Frequency (Hz)\tAmplitude");
    for (let i = 0; i < frequencies.length; i++) {
        console.log(`${frequencies[i]}\t${amplitudes[i]}`);
    }
}

const testCases = [
    { f: [100], a: [1] },
    { f: [100, 300, 700], a: [1, 1, 1] },
    { f: [100, 300, 700], a: [3, 2, 1] }
];

testCases.forEach(({ f, a }, index) => {
    console.log(`Test Case ${index + 1}`);
    let signal = generateSignal(f, a);
    let { frequencies, amplitudes } = dft(signal);
    printForExcel(frequencies, amplitudes);
    console.log("\n");
});