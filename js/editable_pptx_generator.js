/**
 * Editable Editable PPTX Generator for FactorLab Pitch Decks
 * Recreates slides programmatically using PptxGenJS native shapes and text.
 */

class EditablePPTXGenerator {
    constructor() {
        this.pres = null;
        this.isGenerating = false;
    }

    async loadDependencies() {
        if (!window.PptxGenJS) {
            await this.loadScript('https://cdn.jsdelivr.net/gh/gitbrent/pptxgenjs@3.12.0/dist/pptxgen.bundle.js');
        }
    }

    loadScript(src) {
        return new Promise((resolve, reject) => {
            const script = document.createElement('script');
            script.src = src;
            script.onload = resolve;
            script.onerror = reject;
            document.head.appendChild(script);
        });
    }

    async generate(buttonElement) {
        if (this.isGenerating) return;
        this.isGenerating = true;

        const originalText = buttonElement.innerHTML;
        buttonElement.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Generating PPTX...';
        buttonElement.disabled = true;

        try {
            await this.loadDependencies();
            this.pres = new PptxGenJS();
            this.pres.layout = 'LAYOUT_16x9';
            // Theme Colors
            this.colors = {
                gold: 'F59E0B',
                darkGold: 'B45309',
                blue: '1E3A8A',
                slate900: '0f172a',
                slate600: '475569',
                bgGradient: { type: 'solid', color: 'F8FAFC' }
            };

            // --- Slide 1: Introduction (Split Layout) ---
            this.buildSlide1();

            // --- Slide 2: PRISM Framework ---
            this.buildSlide2();

            // --- Slide 3: Dual Momentum ---
            this.buildSlide3();

            // --- Slide 4: Adaptive Asset Allocation (3 Pie Layout) ---
            this.buildSlide4();

            // --- Slide 5: The Team ---
            this.buildSlide5();


            // Save
            this.pres.writeFile({ fileName: 'FactorLab_Smallcase_Editable.pptx' });

            buttonElement.innerHTML = '<i class="fas fa-check"></i> Done!';
            setTimeout(() => {
                buttonElement.innerHTML = originalText;
                buttonElement.disabled = false;
                this.isGenerating = false;
            }, 2000);

        } catch (err) {
            console.error(err);
            alert("Error generating PPTX: " + err);
            buttonElement.innerHTML = '<i class="fas fa-exclamation-triangle"></i> Error';
            this.isGenerating = false;
        }
    }

    // =========================================================================
    // SLIDE BUILDERS (Manual Layout Recreation)
    // =========================================================================

    // --- Slide 1: Philosophy (Split Layout) ---
    buildSlide1() {
        let slide = this.pres.addSlide();
        slide.background = { color: 'F8FAFC' };

        // -- Background Blobs --
        slide.addShape(this.pres.ShapeType.ellipse, { x: 9.0, y: -2, w: 6, h: 6, fill: { color: 'DBEAFE', transparency: 60 }, line: 'none' });
        slide.addShape(this.pres.ShapeType.ellipse, { x: -2.0, y: 5, w: 6, h: 6, fill: { color: 'FEF3C7', transparency: 60 }, line: 'none' });

        // -- LEFT: Branding --
        slide.addText("LIVE ON SMALLCASE", { x: 0.5, y: 2.0, w: 3, h: 0.3, color: 'D97706', fontSize: 10, bold: true, tracking: 10 });
        slide.addText("FactorLab", { x: 0.5, y: 2.3, w: 5, h: 0.8, color: '0F172A', fontSize: 54, bold: true, fontFace: 'Montserrat' });
        slide.addText("Strategies", { x: 0.5, y: 3.0, w: 5, h: 0.8, color: '1E3A8A', fontSize: 54, bold: true, fontFace: 'Montserrat' });

        // Border left line
        slide.addShape(this.pres.ShapeType.line, { x: 0.6, y: 4.0, w: 0.0, h: 1.0, line: { color: 'F59E0B', width: 3 } });
        slide.addText([
            { text: "Systematic Wealth Creation.\n", options: { color: '475569' } },
            { text: "Scientifically Engineered.", options: { color: '1E3A8A', bold: true } }
        ], { x: 0.8, y: 4.0, w: 5, h: 1.0, fontSize: 20, fontFace: 'Inter' });

        // Rocket Icon Visual
        slide.addShape(this.pres.ShapeType.roundRect, { x: 0.5, y: 5.5, w: 0.8, h: 0.8, fill: 'FFFFFF', shadow: { type: 'outer', color: '000000', opacity: 0.1 } });
        // (Icon placeholder)
        slide.addText("20+ Years\nBacktested", { x: 1.4, y: 5.5, w: 2, h: 0.8, fontSize: 10, color: '64748B', bold: true });


        // -- RIGHT: Philosophy List --
        // Vertical Divider
        slide.addShape(this.pres.ShapeType.line, { x: 6.5, y: 1.0, w: 0.0, h: 5.5, line: { color: 'CBD5E1', width: 1 } });

        slide.addText("DESIGN PHILOSOPHY", { x: 7.0, y: 1.5, w: 3, h: 0.3, color: '94A3B8', fontSize: 10, bold: true, tracking: 15 });

        let listX = 7.0;
        let listY = 2.2;
        let gap = 1.3;

        // 1. Rule Clarity
        slide.addShape(this.pres.ShapeType.roundRect, { x: listX, y: listY, w: 0.5, h: 0.5, fill: 'DBEAFE' }); // Icon bg
        slide.addText("Rule Clarity", { x: listX + 0.7, y: listY, w: 3, h: 0.5, fontSize: 16, bold: true, color: '0F172A' });
        slide.addText("Every entry, exit, and rebalance is algorithmically defined.", { x: listX + 0.7, y: listY + 0.4, w: 5, h: 0.5, fontSize: 11, color: '475569' });

        // 2. Agility
        slide.addShape(this.pres.ShapeType.roundRect, { x: listX, y: listY + gap, w: 0.5, h: 0.5, fill: 'FEF3C7' }); // Icon bg
        slide.addText("Agility", { x: listX + 0.7, y: listY + gap, w: 3, h: 0.5, fontSize: 16, bold: true, color: '0F172A' });
        slide.addText("Adapts to volatility & momentum decay via multi-signal drivers.", { x: listX + 0.7, y: listY + gap + 0.4, w: 5, h: 0.5, fontSize: 11, color: '475569' });

        // 3. Protection First
        slide.addShape(this.pres.ShapeType.roundRect, { x: listX, y: listY + gap * 2, w: 0.5, h: 0.5, fill: 'D1FAE5' }); // Icon bg
        slide.addText("Protection First", { x: listX + 0.7, y: listY + gap * 2, w: 3, h: 0.5, fontSize: 16, bold: true, color: '0F172A' });
        slide.addText("Returns are secondary to capital survival.", { x: listX + 0.7, y: listY + gap * 2 + 0.4, w: 5, h: 0.5, fontSize: 11, color: '475569' });

    }

    // --- Slide 2: PRISM Framework ---
    buildSlide2() {
        let slide = this.pres.addSlide();
        slide.background = { color: 'F8FAFC' };

        slide.addText("Strategy Intelligence Framework", { x: 0.5, y: 0.5, w: 10, h: 0.8, color: '0F172A', fontSize: 32, bold: true });
        slide.addText("Rigorous validation before capital deployment.", { x: 0.5, y: 1.2, w: 10, h: 0.4, color: '64748B', fontSize: 14 });

        // Central Core
        slide.addShape(this.pres.ShapeType.ellipse, { x: 5.8, y: 3.0, w: 1.8, h: 1.8, fill: '1E3A8A' });
        slide.addText("PRISM", { x: 5.8, y: 3.6, w: 1.8, h: 0.4, align: 'center', color: 'FFFFFF', bold: true, fontSize: 14 });
        slide.addText("Risk & Intelligence", { x: 5.8, y: 3.9, w: 1.8, h: 0.3, align: 'center', color: 'CBD5E1', fontSize: 8 });

        // Satellites
        // Top Left
        slide.addShape(this.pres.ShapeType.line, { x: 4.5, y: 2.5, w: 1.5, h: 1.0, line: 'CBD5E1' }); // Connector
        slide.addShape(this.pres.ShapeType.roundRect, { x: 1.5, y: 1.8, w: 3.5, h: 1.2, fill: 'FFFFFF', line: 'E2E8F0', shadow: { type: 'outer', color: '000000', blur: 5, offset: 2, opacity: 0.1 } });
        slide.addText("Signal Vetting", { x: 1.7, y: 1.9, w: 3, h: 0.3, bold: true, fontSize: 12, color: '0F172A' });
        slide.addText("Refined through multi-regime backtesting.", { x: 1.7, y: 2.3, w: 3, h: 0.5, fontSize: 10, color: '64748B' });

        // Top Right
        slide.addShape(this.pres.ShapeType.line, { x: 7.5, y: 3.0, w: 1.2, h: -0.8, line: 'CBD5E1' });
        slide.addShape(this.pres.ShapeType.roundRect, { x: 8.5, y: 1.8, w: 3.5, h: 1.2, fill: 'FFFFFF', line: 'E2E8F0', shadow: { type: 'outer', color: '000000', blur: 5, offset: 2, opacity: 0.1 } });
        slide.addText("Stress Simulations", { x: 8.7, y: 1.9, w: 3, h: 0.3, bold: true, fontSize: 12, color: '0F172A' });
        slide.addText("Rebalance impact analysis across market conditions.", { x: 8.7, y: 2.3, w: 3, h: 0.5, fontSize: 10, color: '64748B' });

        // Bottom Left
        slide.addShape(this.pres.ShapeType.line, { x: 4.5, y: 4.0, w: 1.5, h: 1.2, line: 'CBD5E1' });
        slide.addShape(this.pres.ShapeType.roundRect, { x: 1.5, y: 5.0, w: 3.5, h: 1.2, fill: 'FFFFFF', line: 'E2E8F0', shadow: { type: 'outer', color: '000000', blur: 5, offset: 2, opacity: 0.1 } });
        slide.addText("Health Monitoring", { x: 1.7, y: 5.1, w: 3, h: 0.3, bold: true, fontSize: 12, color: '0F172A' });
        slide.addText("Ongoing check of signal health & correlations.", { x: 1.7, y: 5.5, w: 3, h: 0.5, fontSize: 10, color: '64748B' });

        // Bottom Right
        slide.addShape(this.pres.ShapeType.line, { x: 7.5, y: 4.0, w: 1.5, h: 1.2, line: 'CBD5E1' });
        slide.addShape(this.pres.ShapeType.roundRect, { x: 8.5, y: 5.0, w: 3.5, h: 1.2, fill: 'FFFFFF', line: 'E2E8F0', shadow: { type: 'outer', color: '000000', blur: 5, offset: 2, opacity: 0.1 } });
        slide.addText("Risk Limits", { x: 8.7, y: 5.1, w: 3, h: 0.3, bold: true, fontSize: 12, color: '0F172A' });
        slide.addText("Concentration limits & drawdown behavior analysis.", { x: 8.7, y: 5.5, w: 3, h: 0.5, fontSize: 10, color: '64748B' });
    }

    // --- Slide 3: Dual Momentum ---
    buildSlide3() {
        let slide = this.pres.addSlide();
        slide.background = { color: 'F8FAFC' };

        slide.addText("Strategy 1", { x: 0.5, y: 0.5, w: 4, h: 0.3, color: this.colors.darkGold, fontSize: 12, bold: true });
        slide.addText("Dual Momentum Model", { x: 0.5, y: 0.8, w: 8, h: 0.8, color: this.colors.slate900, fontSize: 36, bold: true });

        // Key Points
        let startY = 2.0;
        slide.addText("Strongest Asset Selection: Identifies strongest asset class.", { x: 0.5, y: startY, w: 5, h: 0.5, color: '475569', fontSize: 12, bold: true });
        slide.addText("Safety Switch: Shifts to safety on trend reversals.", { x: 0.5, y: startY + 0.8, w: 5, h: 0.5, color: '475569', fontSize: 12, bold: true });
        slide.addText("20+ Years Backtested: Proven across cycles.", { x: 0.5, y: startY + 1.6, w: 5, h: 0.5, color: '475569', fontSize: 12, bold: true });

        // Simplified Diagram visual for consistency
        slide.addShape(this.pres.ShapeType.rightArrow, { x: 6.0, y: 3.0, w: 1.5, h: 0.8, fill: 'DBEAFE' });
        slide.addText("Asset Scan", { x: 6.0, y: 3.0, w: 1.2, h: 0.8, align: 'center', fontSize: 10 });

        slide.addShape(this.pres.ShapeType.rightArrow, { x: 8.0, y: 3.0, w: 1.5, h: 0.8, fill: 'DBEAFE' });
        slide.addText("Stock Pick", { x: 8.0, y: 3.0, w: 1.2, h: 0.8, align: 'center', fontSize: 10 });

        slide.addShape(this.pres.ShapeType.roundRect, { x: 10.0, y: 2.8, w: 1.5, h: 1.2, fill: 'D1FAE5', line: '10B981' });
        slide.addText("Success", { x: 10.0, y: 3.0, w: 1.5, h: 0.8, align: 'center', fontSize: 12, bold: true, color: '065F46' });
    }

    // --- Slide 4: Adaptive Asset Allocation (3 Pie Layout) ---
    buildSlide4() {
        let slide = this.pres.addSlide();
        slide.background = { color: 'F8FAFC' };

        slide.addText("Strategy 2", { x: 0.5, y: 0.5, w: 4, h: 0.3, color: this.colors.darkGold, fontSize: 12, bold: true });
        slide.addText("Adaptive Asset Allocation", { x: 0.5, y: 0.8, w: 8, h: 0.8, color: this.colors.slate900, fontSize: 36, bold: true });

        // Content
        // Reduced width to make room for charts
        slide.addText("Portfolio Autopilot", { x: 0.5, y: 2.0, w: 3.5, h: 0.5, color: '1E3A8A', fontSize: 18, bold: true });
        slide.addText("Shifts smoothly between equity, gold, and debt.", { x: 0.5, y: 2.5, w: 3.5, h: 1.0, color: '475569', fontSize: 12 });

        // Charts Visual (3 Horizontal Pies)
        // Adjusted coordinates to fit in 10-inch width
        let chartY = 2.5;
        let chartW = 1.7;
        let chartH = 1.7;
        let chartGap = 1.9;
        let startX = 4.2;

        // Common Chart Options
        let opts = { showLegend: false, chartColors: ['10B981', 'F59E0B', '64748B'], holeSize: 60 };

        // 1. Bull
        let dataBull = [{ name: "Alloc", labels: ["Equity", "Gold", "Debt"], values: [80, 10, 10] }];
        slide.addChart(this.pres.charts.DOUGHNUT, dataBull, { x: startX, y: chartY, w: chartW, h: chartH, ...opts });
        slide.addText("Bull Regime\n(Aggressive)", { x: startX, y: chartY + 1.5, w: chartW, h: 0.6, align: 'center', fontSize: 9, color: '059669', bold: true });

        // 2. Sideways
        let dataSide = [{ name: "Alloc", labels: ["Equity", "Gold", "Debt"], values: [50, 30, 20] }];
        slide.addChart(this.pres.charts.DOUGHNUT, dataSide, { x: startX + chartGap, y: chartY, w: chartW, h: chartH, ...opts });
        slide.addText("Sideways\n(Balanced)", { x: startX + chartGap, y: chartY + 1.5, w: chartW, h: 0.6, align: 'center', fontSize: 9, color: '1E40AF', bold: true });

        // 3. Bear
        let dataBear = [{ name: "Alloc", labels: ["Equity", "Gold", "Debt"], values: [10, 50, 40] }];
        slide.addChart(this.pres.charts.DOUGHNUT, dataBear, { x: startX + chartGap * 2, y: chartY, w: chartW, h: chartH, ...opts });
        slide.addText("Bear Regime\n(Defensive)", { x: startX + chartGap * 2, y: chartY + 1.5, w: chartW, h: 0.6, align: 'center', fontSize: 9, color: 'B45309', bold: true });
    }

    // --- Slide 5: The Team ---
    buildSlide5() {
        let slide = this.pres.addSlide();
        slide.background = { color: 'F8FAFC' };

        // Blobs
        slide.addShape(this.pres.ShapeType.ellipse, { x: 0, y: 0, w: 5, h: 5, fill: { color: 'DBEAFE', transparency: 80 }, line: 'none' });

        slide.addText("Meet the Portfolio Managers", { x: 0.5, y: 0.5, w: 10, h: 0.8, color: this.colors.slate900, fontSize: 32, bold: true });
        slide.addText("Decades of Systematic Investing Experience.", { x: 0.5, y: 1.2, w: 10, h: 0.5, color: '64748B', fontSize: 14 });

        // Card 1: Manisankar
        slide.addShape(this.pres.ShapeType.rect, { x: 1.0, y: 2.0, w: 4.5, h: 3.5, fill: 'FFFFFF', line: 'E2E8F0', shadow: { type: 'outer', opacity: 0.1 } });
        // Image placeholder
        slide.addShape(this.pres.ShapeType.rect, { x: 1.2, y: 2.2, w: 1.2, h: 1.2, fill: 'E2E8F0' });
        slide.addText("Manisankar", { x: 2.6, y: 2.2, w: 2, h: 0.4, bold: true, fontSize: 14 });
        slide.addText("Founder & Architect", { x: 2.6, y: 2.5, w: 2, h: 0.3, fontSize: 10, color: 'D97706' });
        slide.addText("Manisankar has over 15 years of experience in quantitative finance...",
            { x: 1.2, y: 3.6, w: 4, h: 1.5, fontSize: 10, color: '475569' });

        // Card 2: Sekhar
        slide.addShape(this.pres.ShapeType.rect, { x: 6.0, y: 2.0, w: 4.5, h: 3.5, fill: 'FFFFFF', line: 'E2E8F0', shadow: { type: 'outer', opacity: 0.1 } });
        // Image placeholder
        slide.addShape(this.pres.ShapeType.rect, { x: 6.2, y: 2.2, w: 1.2, h: 1.2, fill: 'E2E8F0' });
        slide.addText("Sekhar", { x: 7.6, y: 2.2, w: 2, h: 0.4, bold: true, fontSize: 14 });
        slide.addText("Co-Founder", { x: 7.6, y: 2.5, w: 2, h: 0.3, fontSize: 10, color: 'D97706' });
        slide.addText("Sekhar brings deep expertise in algorithmic trading systems...",
            { x: 6.2, y: 3.6, w: 4, h: 1.5, fontSize: 10, color: '475569' });
    }

}
