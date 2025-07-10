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

import (
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
)

// SimpleFabricSpec defines the desired state of SimpleFabric
type SimpleFabricSpec struct {
	// +eda:ui:title="Pod Number"
	// Number of the DC POD this fabric is deployed to.
	PodNumber string `json:"pod_number"`
	// +eda:ui:title="Location"
	// Physical location of the DC POD this fabric is deployed to.
	Location string `json:"location"`
}

// SimpleFabricStatus defines the observed state of SimpleFabric
type SimpleFabricStatus struct {
	Baz string `json:"baz,omitempty"`
}

// SimpleFabric is the Schema for the simplefabrics API
// +kubebuilder:object:root=true
// +kubebuilder:subresource:status
// +kubebuilder:resource:path=simplefabrics,scope=Namespaced
type SimpleFabric struct {
	metav1.TypeMeta   `json:",inline"`
	metav1.ObjectMeta `json:"metadata,omitempty"`

	Spec   SimpleFabricSpec   `json:"spec,omitempty"`
	Status SimpleFabricStatus `json:"status,omitempty"`
}

// SimpleFabricList contains a list of SimpleFabric
// +kubebuilder:object:root=true
type SimpleFabricList struct {
	metav1.TypeMeta `json:",inline"`
	metav1.ListMeta `json:"metadata,omitempty"`
	Items           []SimpleFabric `json:"items"`
}

func init() {
	SchemeBuilder.Register(&SimpleFabric{}, &SimpleFabricList{})
}
