Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Quantum flux parametron: Invented by Eiichi Goto at the University of Tokyo, the Quantum Flux Parametron (QFP) is an improvement over his earlier parametron based digital logic technology.  Unlike its predecessor, QFP uses superconducting Josephson junctions on integrated circuits to improve speed and energy efficiency enormously.  In some applications, the complexity of the cryogenic cooling system required is negligible compared to the potential speed gains.  While his design makes use of quantum principles, it is not a quantum computer technology, gaining speed only through higher clock speeds.  Apart from the speed advantage over traditional CMOS integrated circuit design is that parametrons can be operated with zero energy loss (no local increase in entropy), making reversible computing possible.  Low energy use and heat generation is critical in supercomputer design, where thermal load per unit volume has become one of the main limiting factors.

EVE/ZeBu: EVE/ZeBu is a provider of hardware-assisted verification tools for functional verification of Application-specific integrated circuits (ASICs) and system on chip (SOC) designs and for validation of embedded software (software driver, Operating System and Application software) ahead of implementation in silicon.  EVE's hardware acceleration and hardware emulation products work in conjunction with Verilog, SystemVerilog, and VHDL-based simulators from Synopsys, Cadence Design Systems and Mentor Graphics.  EVE's flagship product is ZeBu.

XAP processor: The XAP processor is a RISC processor architecture developed by Cambridge Consultants since 1994.  XAP processors are a family of 16-bit and 32-bit cores, all of which are intended for use in an application-specific integrated circuit or ASIC chip design.  XAP processors were designed for use in mixed-signal integrated circuits for sensor or wireless applications including Bluetooth, ZigBee, GPS, RFID or Near Field Communication chips.  Typically these integrated circuits are used in low cost, high volume products that are battery-powered and must have low energy consumption.  There are other applications where XAP processors have been used to good effect, such as wireless sensor networks and medical devices, e.g. hearing aids.

Counter (digital): A counter circuit is usually constructed of a number of flip-flops connected in cascade.  Counters are a very widely used component in digital circuits, and are manufactured as separate integrated circuits and also incorporated as parts of larger integrated circuits.

Dallas Semiconductor: Dallas Semiconductor, acquired by Maxim Integrated Products in 2001, designed and manufactured analog, digital, and mixed-signal semiconductors (integrated circuits, or ICs).  Its specialties included communications products (including T/E and Ethernet products), microcontrollers, battery management, thermal sensing and thermal management, non-volatile random-access memory, microprocessor supervisors, delay lines, silicon oscillators, digital potentiometers, real-time clocks, temperature-compensated crystal oscillators (TCXOs), iButton, and 1-Wire products.  The Dallas, Texas-based company was founded in 1984 and purchased by Maxim Integrated Products in 2001.  Both the Maxim and Dallas Semiconductor brands were actively used until 2007.  Since then, the Maxim name has been used for all new products, though the Dallas Semiconductor brand has been retained for some older products, which can be identified by "DS" at the beginning of their part numbers.

San Diego Gas &amp; Electric: San Diego Gas & Electric (SDG&E) is the utility that provides natural gas and electricity to San Diego County and southern Orange County in southwestern California, United States.  It is owned by Sempra Energy, a Fortune 500 energy services holding company that is based in San Diego.

Beam lead technology: Beam lead technology is a method of fabricating a semiconductor device.  Its original application was to high-frequency silicon switching transistors and high-speed integrated circuits.  It eliminated the labor-intensive wire-bonding process used for integrated circuits at the time, and allowed automated assembly of semiconductor chips onto larger substrates to produce hybrid integrated circuits.

Sempra Energy: Sempra Energy is an American natural gas utilities holding company based in San Diego, California.  It divides its interests into two broad categories: California utilities, including Southern California Gas Company (SoCalGas) and San Diego Gas & Electric (SDG&E); and businesses not subject to California utilities regulation, chiefly Sempra International and Sempra U.S. Gas & Power.

Synopsys: Synopsys, Inc., an American company, is the leading company by sales in the Electronic Design Automation industry.  Synopsys' first and best-known product is Design Compiler, a logic-synthesis tool.  Synopsys offers a wide range of other products used in the design of an application-specific integrated circuit.  Products include logic synthesis, behavioral synthesis, place and route, static timing analysis, formal verification, hardware description language (SystemC, SystemVerilog/Verilog, VHDL) simulators as well as transistor-level circuit simulation.  The simulators include development and debugging environments which assist in the design of the logic for chips and computer systems.

List of LM-series integrated circuits: The following is a list of LM-series integrated circuits.  Many were among the first analog integrated circuits commercially produced; some were groundbreaking innovations, and many are still being used.  The LM series originated with integrated circuits made by National Semiconductor.  The prefix LM stands for "linear monolithic", referring to the analog components integrated onto a single piece of silicon.  Because of the popularity of these parts, many of them were second-sourced by other manufacturers who kept the sequence number as an aid to identification of compatible parts.  Several generations of pin-compatible descendants of the original parts have since become "de facto" standard electronic components.

Question: Which is a company that makes products for integrated circuits, Synopsys or Sempra Energy?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "company_name": {
      "type": "string",
      "description": "The name of the company that makes products for integrated circuits."
    },
    "is_integrated_circuit_product_provider": {
      "type": "boolean",
      "description": "True if the company provides products or services for integrated circuits, false otherwise."
    },
    "company_industry": {
      "type": "string",
      "description": "The primary industry of the company."
    },
    "integrated_circuit_related_products": {
      "type": "array",
      "description": "A list of specific products or services the company offers related to integrated circuits.",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "company_name",
    "is_integrated_circuit_product_provider",
    "company_industry",
    "integrated_circuit_related_products"
  ],
  "additionalProperties": false
}
