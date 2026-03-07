package com.detector.backend.entity

import jakarta.persistence.Column
import jakarta.persistence.Entity
import jakarta.persistence.GeneratedValue
import jakarta.persistence.GenerationType
import jakarta.persistence.Id
import jakarta.persistence.Table
import org.springframework.security.core.GrantedAuthority
import org.springframework.security.core.authority.SimpleGrantedAuthority
import org.springframework.security.core.userdetails.UserDetails

@Entity
@Table(name = "users")
class User(
    // identity -> quem gera o id é o banco de dados, não a aplicação
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY) 
    val id: Long? = null,
    
    @Column(unique = true, nullable = false)
    val usernameField: String,
    
    @Column(nullable = false)
    val passwordField: String,
    
    @Column(nullable = false)
    val role: String = "ROLE_USER"
) : UserDetails {
    override fun getAuthorities(): Collection<GrantedAuthority> = listOf(SimpleGrantedAuthority(role))
    override fun getPassword(): String = passwordField
    override fun getUsername(): String = usernameField
    override fun isAccountNonExpired(): Boolean = true
    override fun isAccountNonLocked(): Boolean = true
    override fun isCredentialsNonExpired(): Boolean = true
    override fun isEnabled(): Boolean = true
}