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
Manual memory management: In computer science, manual memory management refers to the usage of manual instructions by the programmer to identify and deallocate unused objects, or garbage.  Up until the mid-1990s, the majority of programming languages used in industry supported manual memory management, though garbage collection has existed since 1959, when it was introduced with Lisp.  Today, however, languages with garbage collection such as Java are increasingly popular and the languages Objective-C and Swift provide similar functionality through Automatic Reference Counting.  The main manually managed languages still in widespread use today are C and C++ – see C dynamic memory allocation.

Bluebottle OS: Bluebottle (formerly known as AOS and now as A2) is a modular, object-oriented Operating System with unconventional features.  It has automatic and garbage collected memory management and provides soft real-time features and is developed at ETH Zurich.  It is the next generation Native Oberon, the Oberon operating system for bare PC hardware.  It is small and fast and supports multiprocessor computers.  It is completely based on an upward-compatible dialect of the Oberon programming language called Active Oberon.  Its user interface supports a "point-and-click" metaphor to execute commands from text, similar to clicking hyperlinks in a browser.  The interface is a zooming user interface.  More and detailed information can be found in the Russian wikipedia article about A2 (operating system).

Garbage collection (computer science): In computer science, garbage collection (GC) is a form of automatic memory management.  The "garbage collector", or just "collector", attempts to reclaim "garbage", or memory occupied by objects that are no longer in use by the program.  Garbage collection was invented by John McCarthy around 1959 to simplify manual memory management in Lisp.

Extended memory: In DOS memory management, extended memory refers to memory above the first megabyte (2 bytes) of address space in an IBM PC or compatible with an 80286 or later processor.  The term is mainly used under the DOS and Windows operating systems. DOS programs, running in real mode or virtual x86 mode, cannot directly access this memory, but are able to do so through an application programming interface called the "eXtended Memory Specification" (XMS).  This API is implemented by a driver (such as HIMEM.SYS) or the operating system, which takes care of memory management and copying memory between conventional and extended memory, by temporarily switching the processor into protected mode.  In this context the term "extended memory" may refer to either the whole of the extended memory or only the portion available through this API.

Tracing garbage collection: In computer programming, tracing garbage collection is a form of automatic memory management that consists of determining which objects should be deallocated ("garbage collected") by tracing which objects are "reachable" by a chain of references from certain "root" objects, and considering the rest as "garbage" and collecting them.  Tracing garbage collection is the most common type of garbage collection – so much so that "garbage collection" often refers to tracing garbage collection, rather than other methods such as reference counting – and there are a large number of algorithms used in implementation.

Pintos: Pintos is computer software, a simple instructional operating system framework for the 80x86 processor architecture.  It supports kernel threads, loading and running user programs, and a file system, but it implements all of these in a very simple way.  It was created at Stanford University by Ben Pfaff in 2004.  It originated as a replacement for Not Another Completely Heuristic Operating System (Nachos), a similar system originally developed at UC Berkeley by Thomas E. Anderson, and was designed along similar lines.  Like Nachos, Pintos is intended to introduce undergraduates to concepts in operating system design and implementation by requiring them to implement significant portions of a real operating system, including thread and memory management and file system access.  Pintos also teaches students valuable debugging skills.

ETH Zurich: ETH Zurich (Swiss Federal Institute of Technology in Zurich; German: "Eidgenössische Technische Hochschule Zürich" ) is a science, technology, engineering and mathematics university in the city of Zürich, Switzerland.  Like its sister institution EPFL, it is an integral part of the Swiss Federal Institutes of Technology Domain (ETH Domain) that is directly subordinate to Switzerland's Federal Department of Economic Affairs, Education and Research.  The school was founded by the Swiss Federal Government in 1854 with the stated mission to educate engineers and scientists, serve as a national center of excellence in science and technology and provide a hub for interaction between the scientific community and industry.

Bartok (compiler): Bartok is an optimizing compiler and managed runtime system for Common Intermediate Language (which . NET languages compile to), being developed by Microsoft Research.  It aims to be efficient enough to be usable for writing operating systems.  It provides services such as automatic memory management and garbage collection, threading, and marshalling data to and from native code, as well as verification of CIL code.  Bartok is written in C#, including the garbage collector.  Bartok is being used by Microsoft Research for the implementation of Singularity, a highly-dependable operating system written almost entirely in managed code.

OpenStep: OpenStep is an object-oriented application programming interface (API) specification for a legacy object-oriented operating system, with the basic goal of offering a NeXTSTEP-like environment on a non-NeXTSTEP operating system.  OpenStep was principally developed by NeXT with Sun Microsystems, to allow NeXTSTEP (like) development on Sun's operating systems, specifically Solaris.  NeXT produced a version of OpenStep for their own Mach-based Unix, known as OPENSTEP (all capitalized), as well as a version that ran on Windows NT.  The software libraries that shipped with OPENSTEP are a superset of the original OpenStep specification, including many features from the original NeXTSTEP.

Virtual memory: In computing, virtual memory is a memory management technique that is implemented using both hardware and software.  It maps memory addresses used by a program, called "virtual addresses", into "physical addresses" in computer memory.  Main storage, as seen by a process or task, appears as a contiguous address space or collection of contiguous segments.  The operating system manages virtual address spaces and the assignment of real memory to virtual memory.  Address translation hardware in the CPU, often referred to as a memory management unit or "MMU", automatically translates virtual addresses to physical addresses.  Software within the operating system may extend these capabilities to provide a virtual address space that can exceed the capacity of real memory and thus reference more memory than is physically present in the computer.

Question: Bluebottle (formerly known as AOS and now as A2) is a modular, object-oriented Operating System with unconventional features, it has automatic and garbage collected memory management and provides soft real-time features and is developed at which science, technology, engineering and mathematics university in the city of Zürich, Switzerland?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "operating_system_name": {
      "type": "string",
      "description": "The name of the operating system in question."
    },
    "developer_university": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the university where the OS is developed."
        },
        "location": {
          "type": "string",
          "description": "The city and country where the university is located."
        },
        "type": {
          "type": "string",
          "description": "The type of institution (e.g., science, technology, engineering and mathematics university)."
        }
      },
      "required": [
        "name",
        "location",
        "type"
      ],
      "additionalProperties": false
    },
    "memory_management_type": {
      "type": "string",
      "description": "The type of memory management used by the operating system."
    }
  },
  "required": [
    "operating_system_name",
    "developer_university",
    "memory_management_type"
  ],
  "additionalProperties": false
}
