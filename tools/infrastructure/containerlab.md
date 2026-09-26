# Containerlab

> Declarative container-based network lab orchestration system for simulating complex network topologies.

---

## Purpose
Containerlab provides a CLI interface for orchestrating and managing container-based networking labs. It allows researchers and network engineers to launch virtual routers, network appliances (Nokia SR Linux, Arista cEOS, Cisco XRd, FRR), and client containers in user-defined topologies powered by Docker and Linux network namespaces.

## Category
- **Primary**: Infrastructure & Cloud Assets (`infrastructure`)
- **Secondary**: Workflow Automation & Pipelines (`automation`), Network & IP Intelligence (`network`)

## Interface
- **CLI**

## Language & Runtime
- **Language**: Go (Golang)
- **Platform**: Linux, Docker

## Installation

```bash
# Official automated installation script
bash -c "$(curl -sL https://get.containerlab.dev)"

# Or install via package manager (Debian/Ubuntu)
echo "deb [trusted=yes] https://apt.fury.io/netdevops/ /" | sudo tee -a /etc/apt/sources.list.d/netdevops.list
sudo apt update && sudo apt install containerlab
```

## Usage

```bash
# Deploy a virtual network lab topology from YAML
sudo containerlab deploy --topo my-lab.clab.yml

# Inspect running lab nodes and interface connections
sudo containerlab inspect --all

# Destroy a lab topology and release resources
sudo containerlab destroy --topo my-lab.clab.yml
```

## Common Use Cases
1. **Network Infrastructure Simulation**: Modeling target enterprise networks and corporate WAN topologies in a sandboxed, isolated environment.
2. **Investigation Lab Deployment**: Rapidly spinning up isolated multi-node testbeds for validating attack surface discoveries and routing paths.
3. **BGP & Telemetry Testing**: Simulating BGP route advertisements and DNS routing behavior prior to live assessments.

## Input
- Declarative YAML topology specification file (`.clab.yml`).

## Output
- Containerized network topology, Linux veth pair linkages, and interactive terminal consoles for each network node.

## Requirements
- **Dependencies**: Linux OS, Docker engine.
- **API Keys**: None required.
- **Account / Authentication**: Elevated privileges (sudo) for namespace manipulation.
- **External Services**: Container registries (Docker Hub, GitHub Container Registry).

## License
- **License**: BSD 3-Clause License

## Source
- **Official Repository**: [https://github.com/srl-labs/containerlab](https://github.com/srl-labs/containerlab)
- **Website / Docs**: [https://containerlab.dev](https://containerlab.dev)

## Status
- **Status**: Active

## RAVEN Notes
Containerlab is the premier utility for infrastructure emulation in RAVEN. When investigating complex organizational perimeters or multi-hop networks, Containerlab allows you to stand up an exact replica of the target's routing architecture inside a local Linux workstation for harmless validation.
