# YAT College — Current ICT Environment

**Relevant to:** S1-CL1 AT1, AT2, AT3

**UoC references this document satisfies:**
- [ICTICT517 AC 5] Information on current ICT systems and practices in the organisation including operating systems, hardware, and security
- [ICTICT517 PC 1.2] Determine and document current state of ICT systems and practices in organisation
- [ICTCLD502 PC 2.1] Review architecture of traditional multi-tier web application in non-cloud environment and identify high availability requirements

**Source status:** ✅ Verbatim from YAT case study (originally in 517 AT2 source)

---

## Network

Network infrastructure (Internet access, routing and switching) is provided with no Single Point of Failure (SPF). All servers and NAS devices have at least 2 NICs and are configured to utilise the redundant network infrastructure. The internal network and the connection to the Internet can accommodate significant load increases without performance degradation.

## Network Services

YAT has deployed Active Directory (AD) 2016 as well as a number of network services (AD, DHCP, DNS). AD and network services are shared across both zones and are installed on multiple systems to ensure a single system server failure will not result in a service outage. A single VPN server provides remote access for staff only. AD and network services can accommodate significant load increases without performance degradation.

## System Management

A single Windows Server 2016 server is used for system management and monitoring purposes and for running daily backups. This server manages systems and backups in both zones. This system does not require high availability.

## Application Services

Accounting and office administration services are provided on a single Windows Server 2016 system. Critical functions (e.g. pay runs) are outsourced to ensure required availability.

## LMS

The LMS runs on Windows Server 2016 and uses a MySQL database. It is installed on a single local server which is at the end of its lifetime. System performance of this mission critical system is expected to degrade noticeably if the load increases.

## Email

Both students and staff use Office 365 for email. Office 365 is a Software as a Service (SaaS) solution hosted in in Microsoft's Azure cloud and is integrated with the on-premises environment.

## Storage

Two NAS servers are deployed at YAT. One is deployed in the student network zone and the other in the staff network zone. All servers deployed at YAT use hot-swappable disks configured using RAID-5. The NAS systems can accommodate significant data growth without degradation of the service. Currently the NAS systems are not considered mission critical, this may however change in future.

## Desktop Computers

Every classroom and staff office are equipped with Desktop Computers connected to the corresponding network zone. All Desktop computers run Windows 10 Enterprise Edition.

## Printers

There is a printer in every classroom. High-performance multifunction printers are available to staff in designated locations.

## Network Security

The network is split into two security zones. Students have access only to resources in the student zone and to the LMS application. Access to network objects in both zones is controlled via AD permissions.

## ICT Facilities

Servers and network devices are located in a physically secured air-conditioned computer room that is protected by an UPS against power loss and electrical surges.

## ICT Staff

ICT staff are highly skilled in their area of expertise and are have excellent subject matter knowledge when dealing with the current environment. However, they lack expertise and experience with cloud technologies.
