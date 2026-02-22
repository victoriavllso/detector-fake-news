package com.detector.backend.controller

import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.RestController
import org.springframework.web.bind.annotation.RequestBody
import org.springframework.web.bind.annotation.CrossOrigin
import org.springframework.web.bind.annotation.PostMapping
import com.detector.backend.service.MLIntegrationService

import reactor.core.publisher.Mono



@RestController
@CrossOrigin(origins = ["\${front.url_front}"]) // permite que o front mande requisições ao back
class PredictionController(private val mlIntegrationService: MLIntegrationService) {

    @PostMapping("/predict")
    fun predict(@RequestBody request: Map<String, String>): Mono<Map<*, *>> {
        val content = request["text"] ?: ""
        return mlIntegrationService.analyzeText(content)
    }
}
