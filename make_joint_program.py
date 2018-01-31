
from conf_misc  import *
from conf_types import *
from conf_html  import *

import argparse
import sys
from typing import *

################################################################################
##### COMPLETE PROGRAM

PROGRAM = Program()

HPCA  = PROGRAM.add_conference('HPCA')
CGO   = PROGRAM.add_conference('CGO')
PPoPP = PROGRAM.add_conference('PPoPP')
CC    = PROGRAM.add_conference('CC')


HPCA_track_1  = PROGRAM.add_track(HPCA)
HPCA_track_2  = PROGRAM.add_track(HPCA)
HPCA_track_3  = PROGRAM.add_track(HPCA)
CGO_track_1   = PROGRAM.add_track(CGO)
CGO_track_2   = PROGRAM.add_track(CGO)
PPoPP_track_1 = PROGRAM.add_track(PPoPP)
PPoPP_track_2 = PROGRAM.add_track(PPoPP)
PPoPP_track_3 = PROGRAM.add_track(PPoPP)
PPoPP_track_4 = PROGRAM.add_track(PPoPP)
PPoPP_track_5 = PROGRAM.add_track(PPoPP)
CC_track_1    = PROGRAM.add_track(CC)

SATURDAY  = datetime.date(2018, 2, 24)
SUNDAY    = datetime.date(2018, 2, 25)
MONDAY    = datetime.date(2018, 2, 26)
TUESDAY   = datetime.date(2018, 2, 27)
WEDNESDAY = datetime.date(2018, 2, 28)


def day_time(day: datetime.date):
  def time(hour, minute):
    return datetime.datetime(day.year, day.month, day.day, hour, minute)

  return time


def session(*, track: Track, **kwargs) -> Session:
  builder = Session_Builder(**kwargs)

  return builder.build(PROGRAM, track)


def joint_event(**kwargs) -> Joint_Event:
  builder = Joint_Event_Builder(**kwargs)

  return builder.build(PROGRAM)


event = Event_Builder


#####
##### SATURDAY
#####

time = day_time(SATURDAY)

joint_event(
  title = 'Registration',
  start = time(8, 0), end = time(18, 15),
)
joint_event(
  title = 'Coffee Break',
  start = time(10, 0), end = time(10, 30),
)
joint_event(
  title = 'Lunch',
  start = time(12, 0), end = time(13, 30),
)
joint_event(
  title = 'Coffee Break',
  start = time(15, 0), end = time(15, 30),
)
joint_event(
  title = 'Departure of the busses to the Heurigen',
  start = time(18, 15),
)
joint_event(
  title = 'Heurigen: Toni & Birgit Nigl',
  link  = 'http://www.nigl.me/index.php?id=25',
  start = time(18, 30),
)

session(
  track  = HPCA_track_1,
  title  = "AACBB: Accelerator Architecture in Computational Biology and Bioinformatics",
  link   = "https://aacbb-workshop.github.io/",
  start  = time(8, 30),
  end    = time(10, 00),
  room   = 'Europa 3',
  events = [
    event(
      title  = "Opening Remarks",
      # people = ["", ]
    ),
    event(
      title  = 'Keynote 1: "Accelerating Genome Analysis: A Primer on an Ongoing Journey"',
      people = ["Onur Mutlu (ETH, CMU)", ]
    ),
    event(
      title  = "Exploring Speed/Accuracy Trade-offs",
      people = ["Mohammed Alser+, Hasan Hassan*, Akash Kumar&, Onur Mutlu* and Can Alkan+ (+Bilkent Univ., *ETH Zurich, &TU Dresden)"]
    ),
    event(
      title  = "Accelerating Duplicate Marking In The Cloud",
      people = ["Lisa Wu, Frank Nothaft, Brendan Sweeney, David Bruns-Smith, Sagar Karandikar, Johnny Le, Howard Mao, Krste Asanovic, David Patterson and Anthony Joseph (UC Berkeley)"]
    ),
  ],
)
session(
  track  = HPCA_track_1,
  title  = "AACBB: Accelerator Architecture in Computational Biology and Bioinformatics",
  link   = "https://aacbb-workshop.github.io/",
  start  = time(10, 30),
  end    = time(12, 10),
  room   = 'Europa 3',
  events = [
    event(
      title  = 'Invited Talk: "Next Generation Sequencing: Big Data meets High Performance Computing Architectures"',
      people = ['Bertil Schmidt (JGU Mainz)']
    ),
    event(
      title  = 'GAME: GPU Acceleration of Metagenomics Clustering',
      people = ["Wenqin Huangfu+, Zhenhua Zhu*, Xing Hu+, Yu Wang* and Yuan Xie+ (+UCSB, *Tsinghua University)", ]
    ),
    event(
      title  = "Exact Alignment with FM-index on the Intel Xeon Phi Knights Landing Processor",
      people = ["Jose M. Herruzo+, Sonia Gonzalez-Navarro+, Pablo Ibañez*, Victor Viñals*, Jesus Alastruey* and Oscar Plata+ (+Univ. of Malaga, *Univ. of Zaragoza)"]
    ),
    event(
      title  = "Optimizations of Sequence Alignment on FPGA: A Case Study of Extended Sequence Alignment",
      people = ["Zheming Jin and Kazutomo Yoshii (ANL)"]
    ),
  ],
)
session(
  track  = HPCA_track_1,
  title  = "AACBB: Accelerator Architecture in Computational Biology and Bioinformatics",
  link   = "https://aacbb-workshop.github.io/",
  start  = time(13, 30),
  end    = time(15, 10),
  room   = 'Europa 3',
  events = [
    event(
      title  = 'Keynote 2: "Automata Processor and its Applications in Bioinformatics"',
      people = ['Srinivas Aluru (Georgia Tech)'],
    ),
    event(
      title  = 'Streaming Gap-Aware Seed Alignment on the Cache Automaton',
      people = ["Tommy Tracy Ii, Jack Wadden, Kevin Skadron and Mircea Stan (UVA)"]
    ),
    event(
      title  = "Processing-in-Storage Architecture for Large-Scale Biological Sequence Alignment",
      people = ["Roman Kaplan, Leonid Yavits and Ran Ginosar (Technion)"],
    ),
    event(
      title  = "The Genomic Benchmark Suite: Characterization and Architecture Implications",
      people = ["Xueqi Li, Guangming Tan, Yuanrong Wang and Ninghui Sun (ICT)", ],
    )
  ],
)
session(
  track  = HPCA_track_1,
  title  = "AACBB: Accelerator Architecture in Computational Biology and Bioinformatics",
  link   = "https://aacbb-workshop.github.io/",
  start  = time(15, 30),
  end    = time(17, 50),
  room   = 'Europa 3',
  events = [
    event(
      title  = 'Invited Talk: "Addressing Computational Burden to Realize Precision Medicine"',
      people = ['Can Alkan (Bilkent University)']
    ),
    event(
      title  = "Burrows-Wheeler Short Read Aligner on AWS EC2 F1",
      people = ["Sergiu Mosanu and Mircea Stan (UVA)"],
    ),
    event(
      title  = "Towards BIMAX: Binary Inclusion-MAXimal parallel implementation for gene expression analysis",
      people = ["Angélica Alejandra Serrano-Rubio, Amilcar Meneses-Viveros, Guillermo B. Morales-Luna",
                "Mireya Paredes-López (CINVESTAV-IPN)"]
    ),
    event(
      title  = 'Memory: The Dominant Bottleneck in Genomic Workloads',
      people = ['Meysam Taassori+, Anirban Nag+, Keeton Hodgson+, Ali Shafiee*',
                'Rajeev Balasubramonian+ (+Univ. of Utah, *Samsung Electronics)'],
    ),
    event(
      title  = 'Gene Sequencing: Where Time Goes',
      people = ['Meysam Roodi and Andreas Moshovos (Univ. of Toronto)'],
    ),
    event(
      title  = 'Are Next-Generation HPC Systems Ready for Population-level Genomics Data Analytics?',
      people = ['Calvin Bulla, Lluc Alvarez and Miquel Moreto (BSC)'],
    ),
    event(
      title = 'Closing remarks',
    ),
  ],
)

session(
  track  = HPCA_track_2,
  title  = "HIPINEB: High-Performance Interconnection Networks in the Exascale and Big-Data Era",
  link   = "http://hipineb.i3a.info/hipineb2018/",
  start  = time(8, 30),
  end    = time(10, 00),
  room   = 'Europa 7',
  events = [
    event(
      title  = "Opening",
    ),
    event(
      title  = 'Keynote: "The three L\'s in modern high-performance networking: Low latency, Low cost, Low processing load"',
      people = ["Torsten Hoefler (ETH Zürich, Switzerland)", ]
    ),
  ],
)
session(
  track  = HPCA_track_2,
  title  = "HIPINEB: High-Performance Interconnection Networks in the Exascale and Big-Data Era",
  link   = "http://hipineb.i3a.info/hipineb2018/",
  start  = time(10, 30),
  end    = time(12, 00),
  room   = 'Europa 7',
  events = [
    event(
      title  = 'Technical Session 1 (research papers)',
    ),
  ],
)
session(
  track  = HPCA_track_2,
  title  = "HIPINEB: High-Performance Interconnection Networks in the Exascale and Big-Data Era",
  link   = "http://hipineb.i3a.info/hipineb2018/",
  start  = time(13, 30),
  end    = time(15, 00),
  room   = 'Europa 7',
  events = [
    event(
      title  = 'Technical Session 2 (research papers)',
    ),
  ],
)
session(
  track  = HPCA_track_2,
  title  = "HIPINEB: High-Performance Interconnection Networks in the Exascale and Big-Data Era",
  link   = "http://hipineb.i3a.info/hipineb2018/",
  start  = time(15, 30),
  end    = time(17, 00),
  room   = 'Europa 7',
  events = [
    event(
      title  = 'Panel Session: "Industrial perspective of high-speed communication technology evolution"',
      people = ['moderated by Prof. Young Cho (University of Southern California)']
    ),
  ],
)

session(
  track  = CGO_track_1,
  title  = "LLVM Tutorial",
  link   = "http://llvm.org/devmtg/2018-02-24/",
  start  = time(8, 30),
  end    = time(10, 00),
  room   = 'Europa 2',
  events = [
    event(
      title  = "Tutorial 1",
    ),
  ],
)
session(
  track  = CGO_track_1,
  title  = "LLVM Tutorial",
  link   = "http://llvm.org/devmtg/2018-02-24/",
  start  = time(10, 30),
  end    = time(12, 00),
  room   = 'Europa 2',
  events = [
    event(
      title  = "Tutorial 2",
    ),
  ],
)
session(
  track  = CGO_track_1,
  title  = "LLVM Performance Workshop",
  link   = "https://sites.google.com/site/realworlddsl/",
  start  = time(13, 30),
  end    = time(15, 00),
  room   = 'Europa 2',
  events = [
    event(
      title  = "Session 1",
    ),
  ],
)
session(
  track  = CGO_track_1,
  title  = "LLVM Performance Workshop",
  link   = "https://sites.google.com/site/realworlddsl/",
  start  = time(15, 30),
  end    = time(17, 00),
  room   = 'Europa 2',
  events = [
    event(title = "Session 2"),
  ],
)

session(
  track  = CGO_track_2,
  title  = "RWDSL'18: 3rd International Workshop on Real World Domain Specific Languages",
  link   = "https://sites.google.com/site/realworlddsl/",
  start  = time(8, 30),
  end    = time(10, 00),
  room   = 'Europa 6',
  events = [
    event(
      title  = "Session 1",
    ),
  ],
)
session(
  track  = CGO_track_2,
  title  = "RWDSL'18: 3rd International Workshop on Real World Domain Specific Languages",
  link   = "https://sites.google.com/site/realworlddsl/",
  start  = time(10, 30),
  end    = time(12, 00),
  room   = 'Europa 6',
  events = [
    event(
      title  = "Session 2",
    ),
  ],
)
session(
  track  = CGO_track_2,
  title  = "RWDSL'18: 3rd International Workshop on Real World Domain Specific Languages",
  link   = "https://sites.google.com/site/realworlddsl/",
  start  = time(13, 30),
  end    = time(15, 00),
  room   = 'Europa 6',
  events = [
    event(
      title  = "Session 3",
    ),
  ],
)
session(
  track  = CGO_track_2,
  title  = "RWDSL'18: 3rd International Workshop on Real World Domain Specific Languages",
  link   = "https://sites.google.com/site/realworlddsl/",
  start  = time(15, 30),
  end    = time(17, 00),
  room   = 'Europa 6',
  events = [
    event(
      title  = "Session 4",
    ),
  ],
)

session(
  track  = PPoPP_track_1,
  title  = "WPMVP: Workshop on Programming Models for SIMD/Vector Processing",
  link   = "https://ppopp18.sigplan.org/track/WPMVP2018",
  start  = time(8, 30),
  end    = time(10, 00),
  room   = 'Europa 5',
  events = [
    event(
      title  = "Keynote TBA",
    ),
    event(
      title  = "Vectorization of a spectral finite-element numerical kernel (Application)",
      people = ["Sylvain Jubertie, Fabrice Dupros, Florent De Martin"]
    ),
  ],
)
session(
  track  = PPoPP_track_1,
  title  = "WPMVP: Workshop on Programming Models for SIMD/Vector Processing",
  link   = "https://ppopp18.sigplan.org/track/WPMVP2018",
  start  = time(10, 30),
  end    = time(12, 00),
  room   = 'Europa 5',
  events = [
    event(
      title  = "Small SIMD Matrices for CERN High Throughput Computing",
      people = ["Florian Lemaitre, Benjamin Couturier, Lionel Lacassagne", ]
    ),
    event(
      title  = "SIMDization of Small Tensor Multiplication Kernels for Wide SIMD Vector Processors",
      people = ["Christopher Rodrigues, Amarin Phaosawasdi, Peng Wu", ]
    ),
    event(
      title  = "MIPP: a Portable C++ SIMD Wrapper and its use for Error Correction Coding in 5G Standard",
      people = ["Adrien Cassagne, Olivier Aumage, Denis Barthou, Camille Leroux, Christophe Jégo", ]
    ),
  ],
)
session(
  track  = PPoPP_track_1,
  title  = "WPMVP: Workshop on Programming Models for SIMD/Vector Processing",
  link   = "https://ppopp18.sigplan.org/track/WPMVP2018",
  start  = time(13, 30),
  end    = time(15, 00),
  room   = 'Europa 5',
  events = [
    event(
      title  = "Ikra-Cpp: A C++/CUDA DSL for Object-Oriented Programming with Structure-of-Arrays Layout",
      people = ["Matthias Springer, Hidehiko Masuhara", ]
    ),
    event(
      title  = "Usuba, Optimizing & Trustworthy Bitslicing Compiler",
      people = ["Darius Mercadier, Lionel Lacassagne, Gilles Muller, Pierre-Evariste Dagand", ]
    ),
    event(
      title  = "A Data Layout Transformation for Vectorizing Compilers",
      people = ["Arsène Pérard-Gayot, Richard Membarth, Philipp Slusallek, Simon Moll, Roland Leißa, Sebastian Hack", ]
    ),
  ],
)
session(
  track  = PPoPP_track_1,
  title  = "WPMVP: Workshop on Programming Models for SIMD/Vector Processing",
  link   = "https://ppopp18.sigplan.org/track/WPMVP2018",
  start  = time(15, 30),
  end    = time(17, 00),
  room   = 'Europa 5',
  events = [
    event(
      title  = "Investigating automatic vectorization for real-time 3D scene understanding",
      people = ["Alexandru Nica, Emanuele Vespa, Pablo González De Aledo, Paul H J Kelly", ]
    ),
    event(
      title  = "Panel Discussion",
      people = ["Jan Eitzinger", ]
    ),
  ],
)

session(
  track  = CC_track_1,
  title  = "CC: International Conference on Compiler Construction Compiler Construction",
  link   = "https://cc-conference.github.io/18/",
  start  = time(8, 30),
  end    = time(10, 00),
  room   = 'Europa 1',
  events = [
    event(title = "Session 1",
    ),
  ],
)
session(
  track  = CC_track_1,
  title  = "CC: International Conference on Compiler Construction Compiler Construction",
  link   = "https://cc-conference.github.io/18/",
  start  = time(10, 30),
  end    = time(12, 00),
  room   = 'Europa 1',
  events = [
    event(
      title   = "Session 2",
    ),
  ],
)
session(
  track  = CC_track_1,
  title  = "CC: International Conference on Compiler Construction Compiler Construction",
  link   = "https://cc-conference.github.io/18/",
  start  = time(13, 30),
  end    = time(15, 00),
  room   = 'Europa 1',
  events = [
    event(
      title   = "Session 3",
    ),
  ],
)
session(
  track  = CC_track_1,
  title  = "CC: International Conference on Compiler Construction Compiler Construction",
  link   = "https://cc-conference.github.io/18/",
  start  = time(15, 30),
  end    = time(17, 00),
  room   = 'Europa 1',
  events = [
    event(
      title   = "Session 4",
    ),
  ],
)


#####
##### SUNDAY
#####

time = day_time(SUNDAY)


joint_event(
  title = 'Registration',
  start = time(8, 0), end = time(18, 30),
)
joint_event(
  title = 'Coffee Break',
  start = time(10, 0), end = time(10, 30),
)
joint_event(
  title = 'Lunch',
  start = time(12, 0), end = time(13, 30),
)
joint_event(
  title = 'Coffee Break',
  start = time(15, 0), end = time(15, 30),
)
joint_event(
  title = 'HPCA/CGO/PPoPP Welcome Reception and Poster Session',
  start = time(18, 00),
)

session(
  track  = HPCA_track_1,
  title  = "WP3: Second Workshop on Pioneering Processor Paradigms",
  link   = 'http://wp3workshop.website/',
  start  = time(8, 30),
  end    = time(10, 00),
  room   = 'Europa 5',
  events = [
    event(title = "Session 1"),
  ],
)
session(
  track  = HPCA_track_1,
  title  = "WP3: Second Workshop on Pioneering Processor Paradigms",
  link   = 'http://wp3workshop.website/',
  start  = time(10, 30),
  end    = time(12, 00),
  room   = 'Europa 5',
  events = [
    event(title = "Session 2"),
  ],
)
session(
  track  = HPCA_track_1,
  title  = "WP3: Second Workshop on Pioneering Processor Paradigms",
  link   = 'http://wp3workshop.website/',
  start  = time(13, 30),
  end    = time(15, 00),
  room   = 'Europa 5',
  events = [
    event(title = "Session 3"),
  ],
)
session(
  track  = HPCA_track_1,
  title  = "WP3: Second Workshop on Pioneering Processor Paradigms",
  link   = 'http://wp3workshop.website/',
  start  = time(15, 30),
  end    = time(17, 00),
  room   = 'Europa 5',
  events = [
    event(title = "Session 4"),
  ],
)

session(
  track  = HPCA_track_2,
  title  = "Accelerating Big Data Processing with Hadoop, Spark and Memcached on Datacenters with Modern Architectures",
  link   = "http://web.cse.ohio-state.edu/~panda.2/hpca18_bigdata_tut.html",
  start  = time(8, 30),
  end    = time(10, 00),
  room   = 'Europa 7',
  events = [
    event(
      title  = "Session 1",
    ),
  ],
)
session(
  track  = HPCA_track_2,
  title  = "Accelerating Big Data Processing with Hadoop, Spark and Memcached on Datacenters with Modern Architectures",
  link   = "http://web.cse.ohio-state.edu/~panda.2/hpca18_bigdata_tut.html",
  start  = time(10, 30),
  end    = time(12, 00),
  room   = 'Europa 7',
  events = [
    event(
      title  = "Session 2",
    ),
  ],
)

session(
  track  = HPCA_track_2,
  title  = "PULP: An open hardware platform, the story so far",
  link   = "http://www.pulp-platform.org/hpca2018/",
  start  = time(13, 30),
  end    = time(15, 00),
  room   = 'Europa 7',
  events = [
    event(
      title  = "PULP concept and goals",
      people = ["Frank K. Gurkaynak", ]
    ),
    event(
      title  = "State of the art of open source hardware design",
      people = ["Frank K. Gurkaynak", ]
    ),
    event(
      title  = "Summary of PULP systems: PULP, PULPino, PULPissimo",
      people = ["Frank K. Gurkaynak", ]
    ),
    event(
      title  = "PULP cores: OR10N, RI5CY, Zero-riscy, Ariane",
      people = ["Florian Zaruba", ]
    ),
  ],
)
session(
  track  = HPCA_track_2,
  title  = "PULP: An open hardware platform, the story so far",
  link   = "http://www.pulp-platform.org/hpca2018/",
  start  = time(15, 30),
  end    = time(17, 30),
  room   = 'Europa 7',
  events = [
    event(
      title  = "Advanced PULP silicon implementations",
      people = ["Francesco Conti", ]
    ),
    event(
      title  = "Acceleration for PULP systems, examples from cryptography and neural networks",
      people = ["Francesco Conti", ]
    ),
    event(
      title  = "PULP Programming",
      people = ["Andreas Kurth", ]
    ),
  ],
)

session(
  track  = HPCA_track_3,
  title  = "Turning HPC clusters into High Performance & High Throughput facilities by using remote GPU virtualization",
  link   = 'https://sites.google.com/site/rcudatutorial/home/hpca2018',
  start  = time(13, 30),
  end    = time(15, 00),
  room   = 'Pacific 2',
  events = [
    event(
      title  = "[Session 1.1] Presentation of remote GPU virtualization techniques and rCUDA features (50 minutes)",
    ),
    event(
      title  = "[Session 1.2] Practical demonstration about how to install and use rCUDA (40 minutes) ",
    ),
  ],
)
session(
  track  = HPCA_track_3,
  title  = "Turning HPC clusters into High Performance & High Throughput facilities by using remote GPU virtualization",
  link   = 'https://sites.google.com/site/rcudatutorial/home/hpca2018',
  start  = time(15, 30),
  end    = time(17, 0),
  room   = 'Pacific 2',
  events = [
    event(
      title = "[Session 2] Guided exercises so that the audience uses rCUDA in a cluster located at Technical University of Valencia, Spain",
    ),
    event(
      title = "Time for attendees to freely exercise with rCUDA in the remote cluster (a set of exercises is proposed)",
    ),
  ],
)

session(
  track  = CGO_track_1,
  title  = "Tutorial: Improving security with reversibility and session types",
  link   = 'http://mrg.doc.ic.ac.uk/tutorials/cgo2018/',
  start  = time(8, 30),
  end    = time(10, 00),
  room   = 'Pacific 3',
  events = [
    event(title = "Session 1",),
  ],
)
session(
  track  = CGO_track_1,
  title  = "Tutorial: Improving security with reversibility and session types",
  link   = 'http://mrg.doc.ic.ac.uk/tutorials/cgo2018/',
  start  = time(10, 30),
  end    = time(12, 00),
  room   = 'Pacific 3',
  events = [
    event(title = "Session 2",),
  ],
)
session(
  track  = CGO_track_1,
  title  = "Tutorial: Improving security with reversibility and session types",
  link   = 'http://mrg.doc.ic.ac.uk/tutorials/cgo2018/',
  start  = time(13, 30),
  end    = time(15, 00),
  room   = 'Pacific 3',
  events = [
    event(title = "Session 3",),
  ],
)
session(
  track  = CGO_track_1,
  title  = "Tutorial: Improving security with reversibility and session types",
  link   = 'http://mrg.doc.ic.ac.uk/tutorials/cgo2018/',
  start  = time(15, 30),
  end    = time(17, 00),
  room   = 'Pacific 3',
  events = [
    event(title = "Session 4",),
  ],
)

session(
  track  = PPoPP_track_1,
  title  = "PMAM: Workshop on Programming Models and Applications for Multicores and Manycores",
  link   = "https://ppopp18.sigplan.org/track/pmam-2018",
  start  = time(8, 30),
  end    = time(10, 00),
  room   = 'Europa 3',
  events = [
    event(title = "Session 1",),
  ],
)
session(
  track  = PPoPP_track_1,
  title  = "PMAM: Workshop on Programming Models and Applications for Multicores and Manycores",
  link   = "https://ppopp18.sigplan.org/track/pmam-2018",
  start  = time(10, 30),
  end    = time(12, 00),
  room   = 'Europa 3',
  events = [
    event(title = "Session 2",),
  ],
)
session(
  track  = PPoPP_track_1,
  title  = "PMAM: Workshop on Programming Models and Applications for Multicores and Manycores",
  link   = "https://ppopp18.sigplan.org/track/pmam-2018",
  start  = time(13, 30),
  end    = time(15, 00),
  room   = 'Europa 3',
  events = [
    event(title = "Session 3",),
  ],
)
session(
  track  = PPoPP_track_1,
  title  = "PMAM: Workshop on Programming Models and Applications for Multicores and Manycores",
  link   = "https://ppopp18.sigplan.org/track/pmam-2018",
  start  = time(15, 30),
  end    = time(17, 00),
  room   = 'Europa 3',
  events = [
    event(title = "Session 4",),
  ],
)

session(
  track  = PPoPP_track_2,
  title  = "GPGPU: Workshop on General Purpose Processing Using GPU",
  link   = "https://gpgpu11.000webhostapp.com/",
  start  = time(8, 30),
  end    = time(10, 00),
  room   = 'Europa 2',
  events = [
    event(title = "Session 1",),
  ],
)
session(
  track  = PPoPP_track_2,
  title  = "GPGPU: Workshop on General Purpose Processing Using GPU",
  link   = "https://gpgpu11.000webhostapp.com/",
  start  = time(10, 30),
  end    = time(12, 00),
  room   = 'Europa 2',
  events = [
    event(title = "Session 2",),
  ],
)
session(
  track  = PPoPP_track_2,
  title  = "GPGPU: Workshop on General Purpose Processing Using GPU",
  link   = "https://gpgpu11.000webhostapp.com/",
  start  = time(13, 30),
  end    = time(15, 00),
  room   = 'Europa 2',
  events = [
    event(title = "Session 3",),
  ],
)
session(
  track  = PPoPP_track_2,
  title  = "GPGPU: Workshop on General Purpose Processing Using GPU",
  link   = "https://gpgpu11.000webhostapp.com/",
  start  = time(15, 30),
  end    = time(17, 00),
  room   = 'Europa 2',
  events = [
    event(title = "Session 4",),
  ],
)

session(
  track  = PPoPP_track_3,
  title  = "An Introduction to Intel® Threading Building Blocks (Intel® TBB) and its Support for Heterogeneous Programming",
  link   = 'https://ppopp18.sigplan.org/event/ppopp-2018-tutorials-an-introduction-to-intel-threading-building-blocks-intel-tbb-and-its-support-for-heterogeneous-programming',
  start  = time(8, 30),
  end    = time(10, 00),
  room   = 'Pacific 1',
  events = [
    event(
      title  = 'Session 1',
      people = ['Rafael Asenjo, Jim Cownie, Aleksei Fedotov'],
    ),
  ],
)
session(
  track  = PPoPP_track_4,
  title  = "Productive parallel programming on FPGA with high-level synthesis",
  link   = 'https://spcl.inf.ethz.ch/Teaching/2018-ppopp/',
  start  = time(8, 30),
  end    = time(10, 00),
  room   = 'Pacific 2',
  events = [
    event(
      title  = "Session 1",
      people = ['Johannes de Fine Licht, Torsten Hoefler'],
    ),
  ],
)
session(
  track  = PPoPP_track_5,
  title  = "Debugging and Profiling Task Parallel Programs with TASKPROF",
  link   = 'https://ppopp18.sigplan.org/event/ppopp-2018-tutorials-debugging-and-profiling-task-parallel-programs-with-taskprof',
  start  = time(8, 30),
  end    = time(10, 00),
  room   = 'Europa 6',
  events = [
    event(
      title  = "Session 1",
      people = ['Santosh Nagarakatte, Adarsh Yoga'],
    ),
  ],
)

session(
  track  = PPoPP_track_3,
  title  = "An Introduction to Intel® Threading Building Blocks (Intel® TBB) and its Support for Heterogeneous Programming",
  link   = 'https://ppopp18.sigplan.org/event/ppopp-2018-tutorials-an-introduction-to-intel-threading-building-blocks-intel-tbb-and-its-support-for-heterogeneous-programming',
  start  = time(10, 30),
  end    = time(12, 00),
  room   = 'Pacific 1',
  events = [
    event(
      title  = 'Session 2',
      people = ['Rafael Asenjo, Jim Cownie, Aleksei Fedotov'],
    ),
  ],
)
session(
  track  = PPoPP_track_4,
  title  = "Productive parallel programming on FPGA with high-level synthesis",
  link   = 'https://spcl.inf.ethz.ch/Teaching/2018-ppopp/',
  start  = time(10, 30),
  end    = time(12, 00),
  room   = 'Pacific 2',
  events = [
    event(
      title  = "Session 2",
      people = ['Johannes de Fine Licht, Torsten Hoefler'],
    ),
  ],
)
session(
  track  = PPoPP_track_5,
  title  = "Debugging and Profiling Task Parallel Programs with TASKPROF",
  link   = 'https://ppopp18.sigplan.org/event/ppopp-2018-tutorials-debugging-and-profiling-task-parallel-programs-with-taskprof',
  start  = time(10, 30),
  end    = time(12, 00),
  room   = 'Europa 6',
  events = [
    event(
      title  = "Session 2",
      people = ['Santosh Nagarakatte, Adarsh Yoga'],
    ),
  ],
)

session(
  track  = PPoPP_track_3,
  title  = "An Introduction to Intel® Threading Building Blocks (Intel® TBB) and its Support for Heterogeneous Programming",
  link   = 'https://ppopp18.sigplan.org/event/ppopp-2018-tutorials-an-introduction-to-intel-threading-building-blocks-intel-tbb-and-its-support-for-heterogeneous-programming',
  start  = time(13, 30),
  end    = time(15, 00),
  room   = 'Pacific 1',
  events = [
    event(
      title  = "Session 3",
      people = ['Rafael Asenjo, Jim Cownie, Aleksei Fedotov'],
    ),
  ],
)
session(
  track  = PPoPP_track_4,
  title  = "High Performance Distributed Deep Learning: A Beginner's Guide",
  link   = 'http://web.cse.ohio-state.edu/~panda.2/ppopp18_dl_tut.html',
  start  = time(13, 30),
  end    = time(15, 00),
  room   = 'Europa 6',
  events = [
    event(
      title  = "Session 1",
      people = ['Dhabaleswar K. Panda, Ammar Ahmad Awan, Subramoni Hari'],
    ),
  ],
)

session(
  track  = PPoPP_track_3,
  title  = "An Introduction to Intel® Threading Building Blocks (Intel® TBB) and its Support for Heterogeneous Programming",
  link   = 'https://ppopp18.sigplan.org/event/ppopp-2018-tutorials-an-introduction-to-intel-threading-building-blocks-intel-tbb-and-its-support-for-heterogeneous-programming',
  start  = time(15, 30),
  end    = time(17, 00),
  room   = 'Pacific 1',
  events = [
    event(
      title  = "Session 4",
      people = ['Rafael Asenjo, Jim Cownie, Aleksei Fedotov'],
    ),
  ],
)
session(
  track  = PPoPP_track_4,
  title  = "High Performance Distributed Deep Learning: A Beginner's Guide",
  link   = 'http://web.cse.ohio-state.edu/~panda.2/ppopp18_dl_tut.html',
  start  = time(15, 30),
  end    = time(17, 00),
  room   = 'Europa 6',
  events = [
    event(
      title  = "Session 2",
      people = ['Dhabaleswar K. Panda, Ammar Ahmad Awan, Subramoni Hari'],
    ),
  ],
)

session(
  track  = CC_track_1,
  title  = "CC: International Conference on Compiler Construction Compiler Construction",
  link   = "https://cc-conference.github.io/18/",
  start  = time(8, 30),
  end    = time(10, 00),
  room   = 'Europa 1',
  events = [
    event(title = "Session 5"),
  ],
)
session(
  track  = CC_track_1,
  title  = "CC: International Conference on Compiler Construction Compiler Construction",
  link   = "https://cc-conference.github.io/18/",
  start  = time(10, 30),
  end    = time(12, 00),
  room   = 'Europa 1',
  events = [
    event(title = "Session 6"),
  ],
)
session(
  track  = CC_track_1,
  title  = "CC: International Conference on Compiler Construction Compiler Construction",
  link   = "https://cc-conference.github.io/18/",
  start  = time(13, 30),
  end    = time(15, 00),
  room   = 'Europa 1',
  events = [
    event(title = "Session 7"),
  ],
)
session(
  track  = CC_track_1,
  title  = "CC: International Conference on Compiler Construction Compiler Construction",
  link   = "https://cc-conference.github.io/18/",
  start  = time(15, 30),
  end    = time(17, 00),
  room   = 'Europa 1',
  events = [
    event(title = "Session 8"),
  ],
)


#####
##### MONDAY
#####

time = day_time(MONDAY)

joint_event(
  title = 'Registration',
  start = time(8, 0), end = time(18, 00),
)
joint_event(
  title = 'Opening',
  start = time(8, 30), end = time(8, 45),
)
joint_event(
  title  = "HPCA Keynote: What is the role of Architecture and Software Researchers on the Road to Quantum Supremacy?",
  link   = "https://hpca2018.ece.ucsb.edu/pages/keynote.html",
  start  = time(8, 45), end = time(9, 55),
  room   = 'Europa 4',
  people = ["Margaret Martonosi (Princeton University)"],
)
joint_event(
  title = 'Coffee Break',
  start = time(9, 55), end = time(10, 20),
)
joint_event(
  title = 'Lunch',
  start = time(11, 45), end = time(13, 15),
)
joint_event(
  title = 'Coffee Break',
  start = time(14, 55), end = time(15, 15),
)
joint_event(
  title = 'Coffee Break',
  start = time(16, 55), end = time(17, 15),
)


session(
  track = HPCA_track_1,
  title = 'Best Paper Session',
  start = time(10, 20),
  end   = time(12, 00),
  room   = 'Europa 4',
  # chair = ,
  events = [
    event(
      title  = "Amdahl's Law in the Datacenter Era: A Market for Fair Processor Allocation",
      people = ['Seyed Majid Zahedi (Duke University)', 'Qiuyun Llull (VMware/Duke University)',
                'Benjamin C. Lee (Duke University)']
    ),
    event(
      title  = "iNPG: Accelerating Critical Section Access with In-Network Packet Generation for NoC based Many-cores",
      people = ["Yuan Yao, Zhonghai Lu (KTH Royal Institute of Technology)"],
    ),
    event(
      title  = "Enabling Efficient Network Service Function Chain Deployment on Heterogeneous Server Platform",
      people = ["Yang Hu (University of Florida/The University of Texas at Dallas)",
                "Tao Li (University of Florida)"],
    ),
    event(
      title  = "Reducing Data Transfer Energy by Exploiting Similarity within a Data Transaction",
      people = ["Donghyuk Lee (NVIDIA)", "Mike O'Connor (NVIDIA / UT-Austin)", "Niladrish Chatterjee (NVIDIA)"],
    ),
  ]
)

session(
  track = HPCA_track_1,
  title = 'Session 2A: Architecture for Neural Network',
  start = time(13, 15),
  end   = time(14, 55),
  room   = 'Europa 4',
  # chair = ,
  events = [
    event(
      title  = "Making Memristive Neural Network Accelerators Reliable",
      people = ['Ben Feinberg (University of Rochester)', 'Shibo Wang (University of Rochester)',
                'Engin Ipek (University of Rochester)'],
    ),
    event(
      title  = "Towards Efficient Microarchitectural Design for Accelerating Unsupervised GAN-based Deep Learning",
      people = ['Mingcong Song', 'Jiaqi Zhang',
                'Huixiang Chen', 'Tao Li (University of Florida)', ]
    ),
    event(
      title  = "Compressing DMA Engine: Leveraging Activation Sparsity for Training Deep Neural Networks",
      people = ["Minsoo Rhu (POSTECH)", "Mike O'Connor (NVIDIA / UT-Austin)", "Niladrish Chatterjee (NVIDIA)",
                "Jeff Pool (NVIDIA)", "Youngeun Kwon (POSTECH)", "Steve Keckler (NVIDIA)"]
    ),
    event(
      title  = "In-situ AI: Towards Autonomous and Incremental Deep Learning for IoT Systems",
      people = ["Mingcong Song (University of Florida)", "Kan Zhong (University of Florida/Chongqing University)",
                "Jiaqi Zhang", "Yang Hu (University of Florida)",
                "Duo Liu (Chongqing University)", "Weigong Zhang (Capital Normal University)",
                "Jing Wang (Capital Normal University)", "Tao Li (University of Florida)"]
    ),
  ]
)

session(
  track = HPCA_track_2,
  title = 'Session 2B: Cache and Memory',
  start = time(13, 15),
  end   = time(14, 55),
  room   = 'Europa 5+6',
  # chair = ,
  events = [
    event(
      title  = "A Hybrid Cache Partitioning-Sharing Technique for Commodity Multicores",
      people = ["Nosayba El-Sayed (CSAIL, MIT (Hosted partially by QCRI, HBKU))",
                "Anurag Mukkara, Po-An Tsai (CSAIL, MIT)", "Harshad Kasture (Oracle)",
                "Xiaosong Ma (QCRI, HBKU)", "Daniel Sanchez (CSAIL, MIT)"]
    ),

    event(
      title  = "SIPT: Speculatively Indexed, Physically Tagged Caches",
      people = ["Tianhao Zheng", "Haishan Zhu", "Mattan Erez (University of Texas at Austin)"]
    ),

    event(
      title  = "Domino Temporal Data Prefetcher",
      people = ["Mohammad Bakhshalipour (Sharif University of Technology)",
                "Pejman Lotfi-Kamran (Institute for Research in Fundamental Sciences (IPM))",
                "Hamid Sarbazi-Azad (Sharif University of Technology)"]
    ),
    event(
      title  = "ProFess: A Probabilistic Hybrid Main Memory Management Framework for High Performance and Fairness",
      people = ["Dmitry Knyaginin (Chalmers University of Technology)",
                "Vassilis Papaefstathiou (FORTH-ICS)", "Per Stenstrom (Chalmers University of Technology)"]
    ),
  ]
)

session(
  track  = HPCA_track_1,
  title  = "Session 3A: Security",
  start  = time(15, 15),
  end    = time(16, 55),
  room   = 'Europa 4',
  events = [
    event(
      title  = "RCoal: Mitigating GPU Timing Attack via Subwarp-based Randomized Coalescing Techniques",
      people = ["Gurunath Kadam (College of William and Mary)", "Danfeng Zhang (Penn State)",
                "Adwait Jog (College of William and Mary)"],
    ),
    event(
      title  = "Are Coherence Protocol States vulnerable to Information Leakage?",
      people = ["Fan Yao, Milos Doroslovacki, Guru Venkataramani (George Washington University)"],
    ),
    event(
      title  = "Record-Replay Architecture as a General Security Framework",
      people = ["Yasser Shalabi, Mengjia Yan (University of Illinois at Urbana-Champaign)",
                "Nima Honarmand (Stony Brook University), Ruby B Lee (Princeton University)",
                "Josep Torrellas (University of Illinois at Urbana-Champaign)"],
    ),
    event(
      title  = "The DRAM Latency PUF: Quickly Evaluating Physical Unclonable Functions by Exploiting the Latency-Reliability Tradeoff in Modern DRAM Devices",
      people = ["Jeremie S Kim (Carnegie Mellon University)", "Minesh Patel, Hasan Hassan (ETH Zurich)",
                "Onur Mutlu (ETH Zurich; Carnegie Mellon University)"],
    ),
  ]
)

session(
  track  = HPCA_track_2,
  title  = "Session 3B: GPU Cache and Memory",
  start  = time(15, 15),
  end    = time(16, 55),
  room   = 'Europa 5+6',
  events = [
    event(
      title  = "Accelerate GPU Concurrent Kernel Execution by Mitigating Memory Pipeline Stalls",
      people = ["Hongwen Dai, Zhen Lin, Chao Li (North Carolina State University)",
                "Chen Zhao, Fei Wang, Nanning Zheng (Xi'an Jiaotong University)",
                "Huiyang Zhou (North Carolina State University)"]
    ),
    event(
      title  = "LATTE-CC: Latency Tolerance Aware Adaptive Cache Compression Management for Energy Efficient GPUs",
      people = ["Akhil Arunkumar, Shin-Ying Lee, Vignesh Soundararajan, Carole-Jean Wu (Arizona State University)"],
    ),
    event(
      title  = "GETM: high-performance GPU transactional memory via eager conflict detection",
      people = ["Xiaowei Ren, Mieszko Lis (University of British Columbia)", ]

    ),
    event(
      title  = "Efficient and Fair Multi-programming in GPUs via Effective Bandwidth Management",
      people = ["Haonan Wang, Fan Luo, Mohamed Ibrahim (College of William and Mary)",
                "Onur Kayiran (AMD Research), Adwait Jog (College of William and Mary)"]
    ),
  ]
)


session(
  track  = HPCA_track_1,
  title  = "Session 4A: Microarchitecture and Benchmark",
  start  = time(17, 15),
  end    = time(18, 55),
  room   = 'Europa 4',
  events = [
    event(
      title  = "A Novel Register Renaming Technique for Out-of-Order Processors",
      people = ["Hamid Tabani, Jose-Maria Arnau, Jordi Tubella, Antonio Gonzalez (Universitat Politècnica de Catalunya)"]
    ),
    event(
      title  = "Wait of a Decade: Did SPEC CPU 2017 Broaden the Performance Horizon?",
      people = ["Reena Panda, Shuang Song, Joseph Dean, Lizy Kurian John (University of Texas at Austin)"]
    ),
    event(
      title  = "Architectural Support for Task Dependence Management with Flexible Software Scheduling",
      people = ["Emilio Castillo, Lluc Alvarez, Miquel Moreto, Marc Casas (Barcelona Supercomputing Center)",
                "Ramon Beivide, Enrique Vallejo, Jose Luis Bosque (Universidad de Cantabria)",
                "Mateo Valero (Barcelona Supercomputing Center)"]
    ),
    event(
      title  = "GDP: Using Dataflow Properties to Accurately Estimate Interference-free Performance at Runtime",
      people = ["Magnus Jahre (Norwegian University of Science and Technology)",
                "Lieven Eeckhout (Ghent University)"]
    ),
  ],
)

session(
  track  = HPCA_track_2,
  title  = "Session 4B: Persistent and NVM memory",
  start  = time(17, 15),
  end    = time(18, 55),
  room   = 'Europa 5+6',
  events = [
    event(
      title  = "Crash Consistency in Encrypted Non-Volatile Main Memory Systems",
      people = ["Sihang Liu (University of Virginia)",
                "Aasheesh Kolli (University of Michigan/Pennsylvania State University)",
                "Jinglei Ren (Microsoft Research), Samira Khan (University of Virginia)"]
    ),
    event(
      title  = "Adaptive Memory Fusion: Towards Transparent, Agile Integration of Persistent Memory",
      people = ["Dongliang Xue, Chao Li, Linpeng Huang, Chentao Wu (Shanghai Jiao Tong University)",
                "Tianyou Li (Intel Asia Pacific R&D co., LTD)"]
    ),
    event(
      title  = "Efficient Hardware-based Undo+Redo Logging for Persistent Memory Systems",
      people = ["Matheus Ogleari, Ethan Miller, Jishen Zhao (University of California, Santa Cruz)"]
    ),
    event(
      title  = "Enabling Fine-Grain Restricted Coset Coding Through Word-Level Compression for PCM",
      people = ["SeyedMohammad Seyedzadeh, Alex Jones, Rami Melhem (University of Pittsburgh)", ]
    ),
  ],
)

session(
  track  = CGO_track_1,
  title  = "Session 1: Managed Runtimes",
  start  = time(10, 20),
  end    = time(11, 45),
  room   = 'Europa 2',
  events = [
    event(
      title  = "SIMD Intrinsics on Managed Language Runtimes",
      people = ["Alen Stojanov (ETH Zurich)", "Ivaylo Toskov (ETH Zurich)",
                "Tiark Rompf (Purdue University)", "Markus Püschel (ETH Zurich)"],
    ),
    event(
      title  = "CollectionSwitch: A Framework for Efficient and Dynamic Collection Selection",
      people = ["Diego Costa (University of Heidelberg, Germany)",
                "Artur Andrzejak (University of Heidelberg, Germany)"],
    ),
    event(
      title  = "Analyzing and Optimizing Task Granularity on the JVM",
      people = "Andrea Rosà, Eduardo Rosales, and Walter Binder (University of Lugano, Switzerland)"
    ),
  ],
)

session(
  track  = CGO_track_1,
  title  = "Session 2: Resilience and Security",
  start  = time(13, 15),
  end    = time(14, 55),
  room   = 'Europa 2',
  events = [
    event(
      title  = "Automating Efficient Variable-Grained Resiliency for Low-Power IoT Systems",
      people = ["Sara S. Baghsorkhi and Christos Margiolas (Intel, USA)"],
    ),
    event(
      title  = "Resilient Decentralized Android Application Repackaging Detection Using Logic Bombs",
      people = ["Qiang Zeng, Lannan Luo, Zhiyun Qian, Xiaojiang Du, and Zhoujun Li (Temple University, USA; University of South Carolina, USA; University of California at Riverside, USA; Beihang University, China)"]
    ),
    event(
      title  = "nAdroid: Statically Detecting Ordering Violations in Android Applications",
      people = ["Xinwei Fu, Dongyoon Lee, and Changhee Jung (Virginia Tech, USA)", ]
    ),
    event(
      title  = "SGXElide: Enabling Enclave Code Secrecy via Self-Modification",
      people = ["Erick Bauman, Huibo Wang, Mingwei Zhang, and Zhiqiang Lin (University of Texas at Dallas, USA; Intel Labs, USA)", ]
    ),
  ]
)

session(
  track  = CGO_track_1,
  title  = "Session 3: Best Paper Finalists",
  start  = time(15, 15),
  end    = time(16, 55),
  room   = 'Europa 2',
  events = [
    event(
      title  = "Poker: Permutation-based SIMD Execution of Intensive Tree Search by Path Encoding",
      people = ["Feng Zhang and Jingling Xue (UNSW, Australia)", ]
    ),
    event(
      title  = "High Performance Stencil Code Generation with LIFT",
      people = ["Bastian Hagedorn, Larisa Stoltzfus, Michel Steuwer, Sergei Gorlatch, and Christophe Dubach (University of Münster, Germany; University of Edinburgh, UK; University of Glasgow, UK)", ]
    ),
    event(
      title  = "Qubit Allocation",
      people = ["Marcos Yukio Siraichi, Vinícius Fernandes dos Santos, Sylvain Collange, and Fernando Magno Quintao Pereira (Federal University of Minas Gerais, Brazil; Inria, France)", ]
    ),
    event(
      title  = "Dominance-based Duplication Simulation (DBDS): Code Duplication to Enable Compiler Optimizations",
      people = ["David Leopoldseder, Lukas Stadler, Thomas Würthinger, Josef Eisl, Doug Simon, and Hanspeter Mössenböck (JKU Linz, Austria; Oracle Labs, Austria; Oracle Labs, Switzerland)", ]
    ),
  ]
)

session(
  track  = PPoPP_track_1,
  title  = "Session 1: Concurrent Data Structures",
  start  = time(10, 20),
  end    = time(11, 45),
  room   = 'Europa 3',
  events = [
    event(
      title  = "Interval-Based Memory Reclamation",
      people = [
        "Haosen Wen  (University of Rochester)"
        "Joseph Izraelevitz  (University of Rochester)"
        "Wentao Cai  (University of Rochester)"
        "Herbert Alan Beadle  (University of Rochester)"
        "Michael Lee Scott  (University of Rochester)"
      ]
    ),
    event(
      title  = "Harnessing Epoch-based Reclamation for Efficient Range Queries",
      people = [
        "Maya Arbel-Raviv  (Technion, Israel Institute of Technology)",
        "Trevor Brown  (Technion, Israel Institute of Technology)",
      ]
    ),
    event(
      title  = "A Persistent Lock-Free Queue for Non-Volatile Memory",
      people = [
        "Michal Friedman  (Technion)",
        "Maurice Herlihy  (Brown University)",
        "Virendra Marathe  (Oracle)",
        "Erez Petrank  (Technion)",
      ],
    ),
  ],
)

session(
  track  = PPoPP_track_1,
  title  = "Session 2: Compilers and runtime systems",
  start  = time(13, 15),
  end    = time(14, 55),
  room   = 'Europa 3',
  events = [
    event(
      title  = "SuperNeurons: Dynamic GPU Memory Management for Training Deep Neural Networks",
      people = [
        "Linnan Wang  (Brown University)",
        "Jinmian Ye  (UESTC)",
        "Yiyang Zhao (UESTC)",
        "Wei WU (UTK)",
        "Ang Li  (PNNL)",
        "Shuaiwen Leon Song  (PNNL)",
        "Zenglin Xu (UESTC)",
        "Tim Kraska  (Brown University)",
      ],
    ),
    event(
      title  = "Juggler: A Dependency-Aware Task Based Execution Framework for GPUs",
      people = [
        "Mehmet E. Belviranli  (Oak Ridge National Laboratory)",
        "Lee Seyong  (Oak Ridge National Laboratory)",
        "Jeffrey S. Vetter  (Oak Ridge National Laboratory)",
        "Laxmi N. Bhuyan  (University of California, Riverside)",
      ]
    ),
    event(
      title  = "HPVM: Heterogeneous Parallel Virtual Machine",
      people = [
        "Maria Kotsifakou  (University of Illinois at Urbana-Champaign)",
        "Prakalp Srivastava  (University of Illinois at Urbana-Champaign)",
        "Matthew D. Sinclair  (University of Illinois at Urbana-Champaign)",
        "Rakesh Komuravelli  (Qualcomm Technologies Inc.)",
        "Vikram Adve  (University of Illinois at Urbana-Champaign)",
        "Sarita Adve  (University of Illinois at Urbana-Champaign)",
      ],
    ),
    event(
      title  = "Hierarchical Memory Management for Mutable State",
      people = [
        "Adrien Guatto  (Carnegie Mellon University)",
        "Sam Westrick  (Carnegie Mellon University)",
        "Ram Raghunathan  (Carnegie Mellon University)",
        "Umut Acar  (Carnegie Mellon University)",
        "Matthew Fluet  (Rochester Institute of Technology)",
      ],
    ),
  ],
)


session(
  track  = PPoPP_track_1,
  title  = "Session 3: Performance",
  start  = time(15, 15),
  end    = time(16, 55),
  room   = 'Europa 3',
  events = [
    event(
      title  = "Bridging the Gap between Deep Learning and Sparse Matrix Format Selection",
      people = [
        "Yue Zhao  (NCSU)",
        "Jiajia Li  (Georgia Tech)",
        "Chunhua Liao  (Lawrence Livermore National Laboratory)",
        "Xipeng Shen  (NCSU)",
      ]
    ),
    event(
      title  = "Optimizing N-Dimensional, Winograd-Based Convolution for Manycore CPUs",
      people = [
        "Zhen Jia  (Princeton University)",
        "Aleksandar Zlateski  (Massachusetts Institute of Technology)",
        "Fredo Durand  (Massachusetts Institute of Technology)",
        "Kai Li  (Princeton University)",
      ]
    ),
    event(
      title  = "vSensor: Leveraging Fixed-Workload Snippets of Programs for Performance Variance Detection",
      people = [
        "Xiongchao Tang  (Tsinghua University)",
        "Jidong Zhai  (Tsinghua University)",
        "Xuehai Qian  (University of Southern California)",
        "Bingsheng He  (National University of Singapore)",
        "Wei Xue  (Tsinghua University)",
        "Wenguang Chen  (Tsinghua University)",
      ]
    ),
  ],
)

session(
  track  = CGO_track_1,
  title  = 'Artifact Evaluation',
  start  = time(17, 15),
  end    = time(17, 45),
  room   = 'Europa 4',
  events = [
    event(title = 'CGO Artifact Evaluation')
  ],
)


session(
  track  = PPoPP_track_1,
  title  = 'Artifact Evaluation',
  start  = time(17, 15),
  end    = time(17, 45),
  room   = 'Europa 3',
  events = [
    event(title = 'PPoPP Artifact Evaluation')
  ],
)


# fake joint event to seperate sessions & business meetings
joint_event(start = time(18, 00),)

session(
  track  = HPCA_track_1,
  start  = time(19, 15),
  end    = time(20, 15),
  events = [
    event(title='HPCA Business Meeting'),
  ],
)

session(
  track  = CGO_track_1,
  start  = time(18, 00),
  end    = time(19, 00),
  events = [event(title="CGO Business Meeting")]
)

session(
  track  = PPoPP_track_1,
  start  = time(18, 00),
  end    = time(19, 00),
  events = [event(title="PPoPP Business Meeting")]
)


#####
##### TUESDAY
#####

time = day_time(TUESDAY)

joint_event(
  title = 'Registration',
  start = time(8, 0), end = time(17, 0),
)
joint_event(
  title = 'Coffee Break',
  start = time(9, 40), end = time(10, 5),
)
joint_event(
  title = 'Lunch',
  start = time(11, 45), end = time(13, 15),
)
joint_event(
  title = 'Women in Academia and Industry Lunch Session',
  room  = 'lunch room',
  link  = 'http://cgo.org/cgo2018/panel/',
  start = time(11, 45), end = time(12, 30),
)
joint_event(
  title = 'Women in Academia and Industry Panel',
  link  = 'http://cgo.org/cgo2018/panel/',
  start = time(12, 35), end = time(13, 10),
  room  = 'Europa 4',
)
joint_event(
  title  = "CGO Keynote: Biological Computation",
  link   = "http://cgo.org/cgo2018/keynotes/#biological-computation",
  start  = time(13, 15), end = time(14, 25),
  room  = 'Europa 4',
  people = ["Sara-Jane Dunn (Microsoft Research Limited)"],
)
joint_event(
  title = 'Coffee Break',
  start = time(14, 25), end = time(14, 50),
)
joint_event(
  title = 'Departure of the busses to Palais Liechtenstein',
  link  = 'https://ppopp18.sigplan.org/attending/banquet',
  start = time(17, 00),
)
joint_event(
  title = 'Banquet at Palais Liechtenstein',
  link  = 'https://ppopp18.sigplan.org/attending/banquet',
  start = time(18, 00),
)

session(
  track  = HPCA_track_1,
  title  = "Session 5A: GPU",
  start  = time(8, 0),
  end    = time(9, 40),
  room  = 'Europa 4',
  events = [
    event(
      title  = "Perception-Oriented 3D Rendering Approximation for Modern Graphics Processors",
      people = ["Chenhao Xie (University of Houston)", "Shuaiwen Leon Song (Pacific Northwest National Laboratory)",
                "Xin Fu (University of Houston)"],
    ),
    event(
      title  = "Warp Scheduling for Fine-Grained Synchronization",
      people = ["Ahmed ElTantawy, Tor Aamodt (University of British Columbia)"]
    ),
    event(
      title  = "WIR: Warp Instruction Reuse to Minimize Repeated Computations in GPUs",
      people = ["Keunsoo Kim, Won Woo Ro (Yonsei University)"]
    ),
    event(
      title  = "G-TSC: Timestamp Based Coherence for GPUs",
      people = ["Abdulaziz Tabbakh, Xuehai Qian, Murali Annavaram (University of Southern California)"]
    ),
  ],
)

session(
  track  = HPCA_track_2,
  title  = "Session 5B: Secure memory",
  start  = time(8, 0),
  end    = time(9, 40),
  room  = 'Europa 5+6',
  events = [
    event(
      title  = "D-ORAM: Path-ORAM Delegation for Low Execution Interference on Cloud Servers with Untrusted Memory",
      people = ["Rujia Wang, Youtao Zhang, Jun Yang (University of Pittsburgh)", ]
    ),
    event(
      title  = "Secure DIMM: Moving ORAM Primitives Closer to Memory",
      people = ["Ali Shafiee, Rajeev Balasubramonian (University of Utah)",
                "Mohit Tiwari (University of Texas at Austin)",
                "Feifei Li (University of Utah)", ]
    ),
    event(
      title  = "Comprehensive VM Protection against Untrusted Hypervisor through Retrofitted AMD Memory Encryption",
      people = ["Yuming Wu, Yutao Liu, Ruifeng Liu, Haibo Chen, Binyu Zang, Haibing Guan (Shanghai Jiao Tong University)", ]
    ),
    event(
      title  = "SYNERGY: Rethinking Secure-Memory Design for Error-Correcting Memories",
      people = ["Gururaj Saileshwar, Prashant Nair (Georgia Institute of Technology)",
                "Prakash Ramrakhyani, Wendy Elsasser (ARM Research)",
                "Moinuddin Qureshi (Georgia Institute of Technology)"]
    ),
  ],
)

session(
  track  = HPCA_track_1,
  title  = "Session 6A: Novel Architecture",
  start  = time(10, 5),
  end    = time(11, 45),
  room  = 'Europa 4',
  events = [
    event(
      title  = "A Case for Packageless Processors",
      people = ["Saptadeep Pal (University of California, Los Angeles)",
                "Daniel Petrisko (University of Illinois Urbana-Champaign)",
                "Adeel Ahmad Bajwa, Puneet Gupta, Subramanian S. Iyer (University of California, Los Angeles),"
                "Rakesh Kumar (University of Illinois Urbana-Champaign)"]
    ),
    event(
      title  = "Extending the Power-Efficiency and Performance of Photonic Interconnects for Heterogeneous Multicores",
      people = ["Scott VanWinkle, Avinash Kodi, Razvan Bunescu (Ohio University)",
                "Ahmed Louri (George Washington University)"]
    ),
    event(
      title  = "Routerless Networks-on-Chip",
      people = ["Fawaz Alazemi, Arash AziziMazreah, Bella Bose, Lizhong Chen (Oregon State University)"]
    ),
    event(
      title  = "HeatWatch: Optimizing 3D NAND Read Operations With Self-Recovery and Temperature Awareness",
      people = ["Yixin Luo, Saugata Ghose (Carnegie Mellon University)",
                "Yu Cai (SK Hynix), Erich F. Haratsch (Seagate Technology)",
                "Onur Mutlu (ETH Zurich)", ]
    ),
  ],
)

session(
  track  = HPCA_track_2,
  title  = "Session 6B: In-Memory Computing",
  start  = time(10, 5),
  end    = time(11, 45),
  room  = 'Europa 5+6',
  events = [
    event(
      title  = "RC-NVM: Enabling Symmetric Row and Column Memory Accesses for In-Memory Databases",
      people = ["Peng Wang (Peking University), Shuo Li (NUDT)",
                "Guangyu Sun, Xiaoyang Wang (Peking University)",
                "Yiran Chen, Hai (Helen) Li (Duke University), Jason Cong (UCLA)",
                "Nong Xiao (NUDT), Tao Zhang (Pennsylvania State University)"]
    ),
    event(
      title  = "GraphR: Accelerating Graph Processing Using ReRAM",
      people = ["Linghao Song (Duke University)", "Youwei Zhuo, Xuehai Qian (University of Southern California)",
                "Miao Hu (Binghamton University SUNY)", "Hai Li, Yiran Chen (Duke University)"]
    ),
    event(
      title  = "GraphP: Reducing Communication of PIM-based Graph Processing with Efficient Data Partition",
      people = ["Mingxing Zhang (Tsinghua University)", "Youwei Zhuo, Chao Wang (University of Southern California)",
                "Mingyu Gao (Stanford University)", "Yongwei Wu, Kang Chen (Tsinghua University)",
                "Christos Kozyrakis (Stanford University), Xuehai Qian (University of Southern California)"]
    ),
    event(
      title  = "PM3: Power Modeling and Power Management for Processing-in-Memory",
      people = ["Chao Zhang, Tong Meng, Guangyu Sun (Peking University)", ]
    ),
  ],
)

session(
  track  = HPCA_track_1,
  title  = "Session 7A: Industry Track",
  start  = time(14, 50),
  end    = time(16, 30),
  room  = 'Europa 4',
  events = [
    event(
      title  = "Don't Correct the Tags in a Cache, just Check their Hamming Distance from the Lookup Tag",
      people = ["Alexander Gendler, Arkady Bramnik, Ariel Szapiro (Intel)",
                "Yiannakis Sazeides (University of Cyprus)"]
    ),
    event(
      title  = "Reliability-aware Data Placement for Heterogeneous Memory Architecture",
      people = ["Manish Gupta (UCSD)", "Vilas Sridharan, David Roberts (AMD)",
                "Andreas Prodromou, Ashish Venkat, Dean Tullsen and Rajesh Gupta (UCSD)", ]
    ),
    event(
      title  = "SmarCo: An Efficient Many-Core Processor for High-Throughput Applications in Datacenters",
      people = ["Dongrui Fan, Wenming Li, Xiaochun Ye, Da Wang, Hao Zhang",
                "Zhimin Tang and Ninghui Sun (Institute of Computing Technology)", ]
    ),
    event(
      title  = "Lost in Abstraction: Pitfalls of Analyzing GPUs at the Intermediate Language Level",
      people = ["Anthony Gutierrez, Bradford M. Beckmann, Alexandru Dutu, Joseph Gross, Michael LeBeane",
                "John Kalamatianos, Onur Kayiran, Matthew Poremba, Brandon Potter, Sooraj Puthoor",
                "Matthew D. Sinclair, Mark Wyse, Jieming Yin, Xianwei Zhang (Advanced Micro Devices)",
                "Akshay Jain, and Timothy Rogers (Purdue University)"]
    ),
  ],
)

session(
  track  = HPCA_track_2,
  title  = "Session 7B: Best of CAL",
  start  = time(14, 50),
  end    = time(16, 30),
  room  = 'Europa 5+6',
  events = [
    event(
      title  = "Resistive Address Decoder",
      people = ["Leonid Yavits, Uri Weiser, and Ran Ginosar (Technion-Israel Institute of Technology)"]
    ),
    event(
      title  = "Transcending Hardware Limits with Software Out-of-order Processing",
      people = ["Trevor Carlson, Kim-Anh Tran, Alexandra Jimborean, Konstantinos Koukos, Magnus Sjalander",
                "Stefanos Kaxiras (Uppsala University and National University of Singapore)"]
    ),
    event(
      title  = "Sensing CPU voltage noise through Electromagnetic Emanations",
      people = ["Zacharias Hadjilambrou, Shidhartha Das, Marcos Antoniades",
                "Yiannakis Sazeides (University of Cyprus and ARM)"]
    ),
  ],
)

session(
  track  = CGO_track_1,
  title  = "Session 4: Linear Algebra and Vectorization",
  start  = time(8, 0),
  end    = time(9, 40),
  room  = 'Europa 2',
  events = [
    event(
      title  = "The Generalized Matrix Chain Algorithm",
      people = ["Henrik Barthels, Marcin Copik, and Paolo Bientinesi (RWTH Aachen University, Germany)"]
    ),
    event(
      title  = "CVR: Efficient Vectorization of SpMV on X86 Processors",
      people = ["Biwei Xie, Jianfeng Zhan, Xu Liu, Wanling Gao, Zhen Jia, Xiwen He",
                "Lixin Zhang (Institute of Computing Technology at Chinese Academy of Sciences, China; College of William and Mary, USA; Princeton University, USA)"]
    ),
    event(
      title  = "Look-Ahead SLP: Auto-vectorization in the Presence of Commutative Operations",
      people = ["Vasileios Porpodas, Rodrigo C. O. Rocha",
                "Luís F. W. Góes (Intel, USA; University of Edinburgh, UK; PUC-MG, Brazil)"]
    ),
    event(
      title  = "Conflict-Free Vectorization of Associative Irregular Applications with Recent SIMD Architectural Advances",
      people = ["Peng Jiang and Gagan Agrawal (Ohio State University, USA; The Ohio State University, USA)"]
    ),
  ],
)

session(
  track  = CGO_track_1,
  title  = "Session 5: Static and Dynamic Analysis",
  start  = time(10, 5),
  end    = time(11, 45),
  room  = 'Europa 2',
  events = [
    event(
      title  = "Scalable Concurrency Debugging with Distributed Graph Processing",
      people = ["Long Zheng, Xiaofei Liao, Hai Jin, Jieshan Zhao",
                "Qinggang Wang (Huazhong University of Science and Technology, China)"]
    ),
    event(
      title  = "Lightweight Detection of Cache Conflicts",
      people = ["Probir Roy, Shuaiwen Leon Song, Sriram Krishnamoorthy",
                "Xu Liu (College of William and Mary, USA; Pacific Northwest National Laboratory, USA)", ]
    ),
    event(
      title  = "CUDAAdvisor: LLVM-Based Runtime Profiling for Modern GPUs",
      people = ["Du Shen, Shuaiwen Leon Song, Ang Li",
                "Xu Liu (College of William and Mary, USA; Pacific Northwest National Laboratory, USA)"]
    ),
    event(
      title  = "May-Happen-in-Parallel Analysis with Static Vector Clocks",
      people = ["Qing Zhou, Lian Li, Lei Wang, Jingling Xue",
                "Xiaobing Feng (Institute of Computing Technology at Chinese Academy of Sciences, China; UNSW, Australia)"]
    ),
  ],
)

session(
  track  = CGO_track_1,
  title  = "Session 6: Memory usage Optimisation",
  start  = time(14, 50),
  end    = time(16, 30),
  room  = 'Europa 2',
  events = [
    event(
      title  = "DeLICM: Scalar Dependence Removal at Zero Memory Cost",
      people = ["Michael Kruse and Tobias Grosser (Inria, France; ETH Zurich, Switzerland)"]
    ),
    event(
      title  = "Loop Transformations Leveraging Hardware Prefetching",
      people = ["Savvas Sioutas, Sander Stuijk, Henk Corporaal, Twan Basten",
                "Lou Somers (Eindhoven University of Technology, Netherlands)"]
    ),
    event(
      title  = "Transforming Loop Chains via Macro Dataflow Graphs",
      people = ["Eddie C. Davis, Michelle Mills Strout",
                "Catherine Olschanowsky (Boise State University, USA; University of Arizona, USA)"]
    ),
    event(
      title  = "Local Memory-Aware Kernel Perforation",
      people = ["Daniel Maier, Biagio Cosenza, and Ben Juurlink (TU Berlin, Germany)"]
    ),
  ],
)

session(
  track  = PPoPP_track_1,
  title  = "Session 4: Best Paper Candidates",
  start  = time(8, 00),
  end    = time(9, 40),
  room   = 'Europa 3',
  events = [
    event(
      title  = "Cache-Tries: Concurrent Lock-Free Hash Tries with Constant-Time Operations",
      people = ["Aleksandar Prokopec  (Oracle Labs)", ]
    ),
    event(
      title  = "Featherlight On-the-fly False-sharing Detection",
      people = [
        "Milind Chabbi  (Hewlett Packard Labs)",
        "Shasha Wen  (College of William and Mary)",
        "Xu LIu  (College of William and Mary)",
      ]
    ),
    event(
      title  = "Register Optimizations for Stencils on GPUs",
      people = [
        "Prashant Singh Rawat  (The Ohio State University)",
        "Aravind Sukumaran-Rajam  (The Ohio State University)",
        "Atanas Rountev  (The Ohio State University)",
        "Fabrice Rastello  (INRIA)",
        "Louis-Noel Pouchet  (Colorado State University)",
        "P. Sadayappan  (The Ohio State University)",
      ]
    ),
    event(
      title  = "FlashR: Parallelize and Scale R for Machine Learning using SSDs",
      people = [
        "Da Zheng  (Johns Hopkins University)",
        "Disa Mhembere  (Johns Hopkins University)",
        "Joshua T. Vogelstein  (Johns Hopkins University)",
        "Carey E. Priebe  (Johns Hopkins University)",
        "Randal Burns  (Johns Hopkins University)",
      ]
    ),
  ],
)

session(
  track  = PPoPP_track_1,
  title  = "Session 5: Concurrency control and fault tolerance",
  start  = time(10, 5),
  end    = time(11, 45),
  room   = 'Europa 3',
  events = [
    event(
      title  = "DisCVar: Discovering Critical Variables Using Algorithmic Differentiation for Transient Faults",
      people = [
        "Harshitha Menon  (Lawrence Livermore National Lab)",
        "Kathryn Mohror  (Lawrence Livermore National Lab)",
      ]
    ),
    event(
      title  = "Practical Concurrent Traversals in Search Trees",
      people = [
        "Dana Drachsler-Cohen  (ETH Zurich)",
        "Martin Vechev  (ETH Zurich)",
        "Eran Yahav  (Technion)",
      ]
    ),
    event(
      title  = "Communication-Avoiding Parallel Minimum Cuts and Connected Components",
      people = [
        "Lukas Gianinazzi  (ETH Zurich)",
        "Pavel Kalvoda  (ETH Zurich)",
        "Alessandro De Palma  (ETH Zurich)",
        "Maciej Besta  (ETH Zurich)",
        "Torsten Hoefler  (ETH Zurich)",
      ]
    ),
    event(
      title  = "Safe Privatization in Transactional Memory",
      people = [
        "Artem Khyzha  (IMDEA Software Institute)",
        "Hagit Attiya  (Technion)",
        "Alexey Gotsman  (IMDEA Software Institute)",
        "Noam Rinetzky  (Tel-Aviv University)",
      ]
    ),
  ],
)

session(
  track  = PPoPP_track_1,
  title  = "Session 6: Models and Libraries",
  start  = time(14, 50),
  end    = time(16, 30),
  room   = 'Europa 3',
  events = [
    event(
      title  = "Making Pull-Based Graph Processing Performant",
      people = [
        "Samuel Grossman  (Stanford University)",
        "Heiner Litz  (UCSC)",
        "Christos Kozyrakis  (Stanford University)",
      ]
    ),
    event(
      title  = "An Effective Fusion and Tile Size Model for Optimizing Image Processing Pipelines",
      people = [
        "Abhinav Jangda  (Indian Institute of Science)",
        "Uday Bondhugula  (Indian Institute of Science)",
      ]
    ),
    event(
      title  = "LazyGraph: Lazy Data Coherency for Replicas in Distributed Graph-Parallel Computation",
      people = [
        "Lei Wang  (Institute of Computing Technology, Chinese Academy of Science)",
        "Liangji Zhuang  (Institute of Computing Technology, Chinese Academy of Science)",
        "Junhang Chen  (Institute of Computing Technology, Chinese Academy of Science)",
        "Huimin Cui  (Institute of Computing Technology, Chinese Academy of Science)",
        "Fang Lv  (Institute of Computing Technology, Chinese Academy of Science)",
        "Ying Liu  (Institute of Computing Technology, Chinese Academy of Science)",
        "Xiaobing Feng  (Institute of Computing Technology, Chinese Academy of Science)",
      ]
    ),
    event(
      title  = "PAM: Parallel Augmented Maps",
      people = [
        "Yihan Sun  (Carnegie Mellon University)",
        "Daniel Ferizovic  (Karlsruhe Institute of Technology)",
        "Guy Blelloch  (Carnegie Mellon University)",
      ]
    ),
  ],
)


#####
##### WEDNESDAY
#####

time = day_time(WEDNESDAY)

joint_event(
  title  = "PPoPP Keynote: From confusion to clarity: hardware concurrency programming models 2008-2018",
  start  = time(8, 0), end = time(9, 0),
  people = ["Peter Sewell (University of Cambridge)"],
  room  = 'Europa 4',
)
joint_event(
  title = 'Coffee Break',
  start = time(9, 0), end = time(9, 25),
)
joint_event(
  title = 'Coffee Break',
  start = time(11, 5), end = time(11, 20),
)

session(
  track  = HPCA_track_1,
  title  = "Session 8A: Industry Track (applications)",
  start  = time(9, 25),
  end    = time(11, 5),
  room  = 'Europa 4',
  events = [
    event(
      title  = "Applied Machine Learning at Facebook: A Datacenter Infrastructure Perspective",
      people = ["Kim Hazelwood, Sarah Bird, David Brooks, Soumith Chintala, Utku Diril, Dmytro Dzhulgakov",
                "Mohamed Fawzy, Bill Jia, Yangqing Jia, Aditya Kalro, James Law, Kevin Lee, Jason Lu",
                "Pieter Noordhuis, Misha Smelyanskiy, Liang Xiong, and Xiaodong Wang (Facebook)", ]
    ),
    event(
      title  = "Amdahl's Law in Big Data Analytics: Alive and Kicking in TPCx-BB (BigBench)",
      people = ["Daniel Richins (The University of Texas at Austin), Tahrina Ahmed (Stanford University)",
                "Russell Clapp (Intel), Vijay Janapa Reddi (Google)", ]
    ),
    event(
      title  = "Memory Hierarchy for Web Search",
      people = ["Grant Ayers (Stanford University), Jung Ho Ahn (Seoul National University)",
                "Christos Kozyrakis (Stanford University), Partha Ranganathan (Google)"]
    ),
    event(
      title  = "Characterizing Resource Sensitivity of Database Workloads",
      people = ["Rathijit Sen and Karthik Ramachandra (Microsoft Corporation)", ]
    ),
  ],
)

session(
  track  = HPCA_track_2,
  title  = "Session 8B: Memory",
  start  = time(9, 25),
  end    = time(11, 5),
  room  = 'Europa 5+6',
  events = [
    event(
      title  = "ERUCA: Efficient DRAM Resource Utilization and Resource Conflict Avoidance for Memory System Parallelism",
      people = ["Sangkug Lym (University of Texas at Austin), Heonjae Ha (Standford University)",
                "Yongkee Kwon (University of Texas at Austin), Chunkai Chang (University of Texas at Austin)",
                "Jungrae Kim (Microsoft)", "Mattan Erez (University of Texas at Austin)"]
    ),
    event(
      title  = "DUO: Dual Use of On-chip Redundancy for High Reliability",
      people = ["Seong-Lyong Gong (UT Austin), Jungrae Kim (Microsoft), Sangkug Lym (UT Austin)",
                "Michael Sullivan (NVIDIA), Howard David (Huawei), Mattan Erez (UT Austin)"]
    ),
    event(
      title  = "Memory System Design for Ultra Low Power, Computationally Error Resilient Processor Microarchitectures",
      people = ["Sriseshan Srikanth (Georgia Institute of Technology), Paul G. Rabbat (Intel Corporation)",
                "Eric R. Hein, Bobin Deng, Thomas M. Conte (Georgia Institute of Technology)",
                "Erik DeBenedictis, Jeanine Cook, Michael P. Frank (Sandia National Laboratories)"]
    ),
    event(
      title  = "NACHOS : Software-Driven Hardware-Assisted Memory Disambiguation for Accelerators",
      people = ["Naveen Vedula, Arrvindh Shriraman, Snehasish Kumar, William N Sumner (Simon Fraser University)"]
    ),
  ],
)

session(
  track  = HPCA_track_1,
  title  = "Session 9A: Accelerators",
  start  = time(11, 20),
  end    = time(12, 35),
  room  = 'Europa 4',
  events = [
    event(
      title  = "OuterSPACE: An Outer product based SPArse matrix multiplication acCElerator",
      people = ["Subhankar Pal, Jonathan Beaumont, Dong-Hyeon Park, Aporva Amarnath",
                "Siying Feng (University of Michigan, Ann Arbor)",
                "Chaitali Chakrabarti (Arizona State University)",
                "Hun-Seok Kim, David Blaauw, Trevor Mudge",
                "Ronald Dreslinski (University of Michigan, Ann Arbor)"]
    ),
    event(
      title  = "Searching for Potential gRNA Off-Target Sites for CRISPR/Cas9 using Automata Processing across Different Platforms",
      people = ["Chunkun Bo, Vinh Dang, Elaheh Sadredini, Kevin Skadron (University of Virginia)"]
    ),
    event(
      title  = "Characterizing and Mitigating Output Reporting Bottlenecks in Spatial-Reconfigurable Automata Processing Architectures",
      people = ["Jack Wadden, Kevin Angstadt, Kevin Skadron (University of Virginia)"]
    ),
  ],
)

session(
  track  = HPCA_track_2,
  title  = "Session 9B: Power",
  start  = time(11, 20),
  end    = time(12, 35),
  room  = 'Europa 5+6',
  events = [
    event(
      title  = "Power and Energy Characterization of an Open Source 25-core Manycore Processor",
      people = ["Michael McKeown, Alexey Lavrov, Mohammad Shahrad, Paul Jackson, Yaosheng Fu",
                "Jonathan Balkind, Tri M. Nguyen, Yanqi Zhou, David Wentzlaff (Princeton University)"]
    ),
    event(
      title  = "A Spot Capacity Market to Increase Power Infrastructure Utilization in Multi-Tenant Data Centers",
      people = ["Mohammad A. Islam (University of California, Riverside)",
                "Xiaoqi Ren (California Institute of Technology)",
                "Shaolei Ren (University of California, Riverside), Adam Wierman (California Institute of Technology)"]
    ),
    event(
      title  = "GPGPU Power Modeling for Multi-Domain Voltage-Frequency Scaling",
      people = ["João Guerreiro, Aleksandar Ilic, Nuno Roma, Pedro Tomás (INESC-ID, Instituto Superior Técnico)"]
    ),
  ],
)

session(
  track  = CGO_track_1,
  title  = "Session 7: Program Generation and Synthesis",
  start  = time(9, 25),
  end    = time(11, 5),
  room   = 'Europa 2',
  events = [
    event(
      title  = "AutoPA: Automatically Generating Active Driver from Original Passive Driver Code",
      people = ["Jia-Ju Bai, Yu-Ping Wang, and Shi-Min Hu (Tsinghua University, China)"]
    ),
    event(
      title  = "Synthesizing an Instruction Selection Rule Library from Semantic Specifications",
      people = ["Sebastian Buchwald, Andreas Fried",
                "Sebastian Hack (KIT, Germany; Saarland University, Germany)"]
    ),
    event(
      title  = "Synthesizing Programs That Expose Performance Bottlenecks",
      people = ["Luca Della Toffola, Michael Pradel",
                "Thomas R. Gross (ETH Zurich, Switzerland; TU Darmstadt, Germany)"]
    ),
    event(
      title  = "Program Generation for Small-Scale Linear Algebra Applications",
      people = ["Daniele G. Spampinato, Diego Fabregat-Traver, Paolo Bientinesi",
                "Markus Püschel (ETH Zurich, Switzerland; RWTH Aachen University, Germany)"]
    ),
  ],
)

session(
  track  = CGO_track_1,
  title  = "Session 8: Compilation for Specialised Domains",
  start  = time(11, 20),
  end    = time(12, 35),
  room   = 'Europa 2',
  events = [
    event(
      title  = "Optimal DNN Primitive Selection with Partitioned Boolean Quadratic Programming",
      people = ["Andrew Anderson and David Gregg (Trinity College Dublin, Ireland)"]
    ),
    event(
      title  = "Register Allocation for Intel Processor Graphics",
      people = ["Wei-Yu Chen, Guei-Yuan Lueh, Pratik Ashar, Kaiyu Chen",
                "Buqi Cheng (Intel, USA; Intel, India)"]
    ),
    event(
      title  = "A Compiler for Cyber-Physical Digital Microfluidic Biochips",
      people = ["Christopher Curtis, Daniel Grissom",
                "Philip Brisk (University of California at Riverside, USA; Azusa Pacific University, USA)"]
    ),
  ],
)

session(
  track  = PPoPP_track_1,
  title  = "Session 7: Parallel frameworks and applications",
  start  = time(9, 25),
  end    = time(11, 5),
  room   = 'Europa 3',
  events = [
    event(
      title  = "Efficient Shuffle Management with SCache for DAG Computing Frameworks",
      people = [
        "Zhouwang Fu  (Shanghai Jiao Tong University)",
        "Tao Song  (Shanghai Jiao Tong University)",
        "Zhengwei Qi  (Shanghai Jiao Tong University)",
        "Haibing Guan  (Shanghai Jiao Tong University)",
      ]
    ),
    event(
      title  = "High-Performance Genomics Data Analysis Framework with In-Memory Computing",
      people = [
        "Xueqi Li  (Institute of Computing Technology, Chinese Academy of Sciences)",
        "Guangming Tan  (Institute of Computing Technology, Chinese Academy of Sciences)",
        "Ninghui Sun  (Institute of Computing Technology, Chinese Academy of Sciences)",
      ]
    ),
    event(
      title  = "Griffin: Uniting CPU and GPU in Information Retrieval Systems for Intra-Query Parallelism",
      people = [
        "Yang Liu  (UC San Diego)",
        "Jianguo Wang  (UC San Diego)",
        "Steven Swanson  (UC San Diego)",
      ]
    ),
    event(
      title  = "swSpTRSV: a Fast Sparse Triangular Solve with Sparse Level Tile Layout on Sunway Architectures",
      people = [
        "Xinliang Wang  (Tsinghua University)",
        "Weifeng Liu  (Norwegian University of Science and Technology)",
        "Wei Xue  (Tsinghua University)",
        "Li Wu  (Tsinghua University)",
      ]
    ),
  ],
)

session(
  track  = PPoPP_track_1,
  title  = "Session 8: Race Detection",
  start  = time(11, 20),
  end    = time(12, 10),
  room   = 'Europa 3',
  events = [
    event(
      title  = "VerifiedFT: A Verified, High-Performance Dynamic Race Detector",
      people = [
        "James R. Wilcox  (University of Washington)",
        "Cormac Flanagan  (UC Santa Cruz)",
        "Stephen N. Freund  (Williams College)",
      ]
    ),
    event(
      title  = "Efficient Parallel Determinacy Race Detection for Two-Dimensional Dags",
      people = [
        "Yifan Xu  (Washington University in St. Louis)",
        "Kunal Agrawal  (Washington University in St. Louis)",
        "I-Ting Angelina Lee  (Washington University in St. Louis)",
      ]
    ),
  ],
)


# fake joint event to seperate sessions & closings
joint_event(start = time(12, 0),)

session(
  track  = HPCA_track_1,
  start  = time(12, 35),
  events = [
    event(title  = "HPCA Closing"),
  ],
)
session(
  track  = CGO_track_1,
  start  = time(12, 35),
  events = [
    event(title = "CGO Closing"),
  ],
)
session(
  track  = PPoPP_track_1,
  start  = time(12, 10),
  events = [
    event(title = "PPoPP Closing"),
  ],
)

joint_event(start = time(13, 0),)


if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  show_people = parser.add_mutually_exclusive_group()

  show_people.add_argument('--show-people', action="store_true", default=True)
  show_people.add_argument('--hide-people', action="store_false", dest='show_people')

  parser.add_argument('--font-size', type=int, default=12)

  full_page = parser.add_mutually_exclusive_group()

  full_page.add_argument('--full-page',  action="store_true", default=True)
  full_page.add_argument('--embeddable', action="store_false", dest='full_page')

  parser.add_argument(
    '-o', '--output',
    type=argparse.FileType('w'),
    default=sys.stdout
  )

  args = parser.parse_args()

  h = HTML(args.output)

  if args.full_page:
    h.print_page_header()

  h.print_program_header(font_size=args.font_size)

  saturday, sunday, monday, tuesday, wednesday = slice_per_day(PROGRAM)

  h.print_day(saturday,  show_people=args.show_people, time_column=False)
  h.print_day(sunday,    show_people=args.show_people, time_column=False)
  h.print_day(monday,    show_people=args.show_people, time_column=True)
  h.print_day(tuesday,   show_people=args.show_people, time_column=True)
  h.print_day(wednesday, show_people=args.show_people, time_column=True)

  h.print_program_footer()

  if args.full_page:
    h.print_page_footer()

  # print_program(
  #   PROGRAM,
  #   dst         = args.output,
  #   show_people = args.show_people,
  #   font_size   = args.font_size,
  #   full_page   = args.full_page,
  # )
