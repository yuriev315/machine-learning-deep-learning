// SOURCE_ONLY: never compiled or run here. Needs macOS, Xcode and an Apple device. Add TinyCNN.mlpackage to the Xcode target;
// Xcode generates the TinyCNN class. Core ML picks CPU, GPU or Neural Engine according to computeUnits.
import CoreML
final class DigitsPredictor {
    private let model: TinyCNN
    init() throws {
        let cfg = MLModelConfiguration()
        cfg.computeUnits = .all
        model = try TinyCNN(configuration: cfg)
    }
    /// pixels: 64 grayscale values scaled to [-1, 1], row by row
    func predict(pixels: [Float]) throws -> (digit: Int, millis: Double) {
        precondition(pixels.count == 64)
        let input = try MLMultiArray(shape: [1, 1, 8, 8], dataType: .float32)
        for (i, p) in pixels.enumerated() { input[i] = NSNumber(value: p) }
        let t0 = CFAbsoluteTimeGetCurrent()
        let out = try model.prediction(input: input).logits
        let ms = (CFAbsoluteTimeGetCurrent() - t0) * 1000
        var best = 0
        for i in 1..<10 where out[i].floatValue > out[best].floatValue { best = i }
        return (best, ms)
    }
}
