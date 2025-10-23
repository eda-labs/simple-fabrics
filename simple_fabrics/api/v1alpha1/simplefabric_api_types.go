/*
Copyright 2025.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

package v1alpha1

// This app demonstrates how developers
// can build abstractions using the existing resources.
// The Simple Fabric application configures the EVPN VXLAN fabric
// with a simplified set of inputs when compared to the Fabrics app.
// It assumes the default values for the node selectors, protocol configuration, etc,
// while exposing a minimal set of parameters to a user.
type SimpleFabricSpec struct {
	// +eda:ui:category="Underlay Network"
	// +eda:ui:title="Underlay ASN Pool"
	// +eda:ui:autocomplete=`{"group":"core.eda.nokia.com", "version":"v1", "resource":"indexallocationpools"}`
	// +kubebuilder:default="asn-pool"
	// The ASN pool used for the underlay network.
	// The `asn-pool` default value is the default ASN pool
	// that comes with "Try EDA" installation.
	UnderlayASNPool string `json:"underlayASNPool"`
}

// SimpleFabricStatus defines the observed state of SimpleFabric
type SimpleFabricStatus struct {
	// The name of the backing Fabric that the Simple Fabric created.
	FabricName string `json:"fabricName,omitempty"`
}
